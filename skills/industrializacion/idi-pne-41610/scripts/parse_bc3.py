#!/usr/bin/env python3
"""
Parser de archivos BC3 (FIEBDC-3) para extracción de presupuestos.
Extrae capítulos, partidas e importes listos para calcular el IdI según PNE 41610.

Uso:
    python parse_bc3.py <archivo.bc3>

Salida JSON con estructura:
{
  "obra": "Nombre de la obra",
  "pem_total": 123456.78,
  "capitulos": [
    {
      "codigo": "01",
      "descripcion": "Estructura",
      "partidas": [
        {
          "codigo": "01.01",
          "descripcion": "Pilares prefabricados de hormigón",
          "unidad": "ud",
          "precio": 850.00,
          "medicion": 12.0,
          "importe": 10200.00,
          "nivel": 2
        }
      ],
      "importe_total": 10200.00
    }
  ]
}
"""

import sys
import json
import re
from pathlib import Path


def detect_encoding(filepath):
    """Detecta la codificación del archivo BC3 (DOS 850 o Windows ANSI)."""
    with open(filepath, 'rb') as f:
        raw = f.read(200)
    # BC3 puede ser CP850 (DOS) o CP1252 (Windows ANSI)
    # Intentar detectar por cabecera ~V
    for enc in ['cp1252', 'cp850', 'utf-8', 'latin-1']:
        try:
            raw.decode(enc)
            return enc
        except UnicodeDecodeError:
            continue
    return 'latin-1'


def parse_bc3(filepath):
    """
    Parsea un archivo BC3 y devuelve estructura de presupuesto.
    
    Registros relevantes:
      ~V  Cabecera / versión
      ~K  Coeficientes (decimales, CI, GG, BI, IVA)
      ~C  Conceptos: capítulos, partidas, materiales, mano de obra
      ~D  Descomposición de precios
      ~M  Mediciones
      ~T  Textos largos
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {filepath}")

    encoding = detect_encoding(filepath)
    
    with open(filepath, encoding=encoding, errors='replace') as f:
        content = f.read()

    # Normalizar saltos de línea y juntar líneas continuadas con \
    lines = content.replace('\r\n', '\n').replace('\r', '\n').split('\n')

    # Diccionario de conceptos: codigo -> {descripcion, unidad, precio, tipo}
    conceptos = {}
    # Árbol jerárquico: codigo_padre -> [codigos_hijos con factor]
    descomposicion = {}  # padre -> [(hijo, rendimiento, precio_factor)]
    mediciones = {}      # codigo -> [(comentario, A, B, C, medicion)]
    obra_nombre = ""
    decimales_precio = 2
    decimales_medicion = 3

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1

        if not line.startswith('~'):
            continue

        # Juntar líneas de continuación (terminan en \)
        while line.endswith('\\') and i < len(lines):
            line = line[:-1] + lines[i].strip()
            i += 1

        tipo = line[1] if len(line) > 1 else ''
        contenido = line[2:] if len(line) > 2 else ''

        if tipo == 'V':
            # ~V|version|programa|cabecera|...
            partes = contenido.split('|')
            if len(partes) > 2:
                obra_nombre = partes[2].strip()

        elif tipo == 'K':
            # ~K|\decimales_precio\...\
            # Formato: ~K|CI\GG\BI\DIVISA\DP\DR\DS\DM\DN\
            partes = contenido.split('|')
            if len(partes) > 1:
                subcampos = partes[1].split('\\')
                # subcampos[4] = decimales precio, subcampos[7] = decimales medición
                try:
                    if len(subcampos) > 4 and subcampos[4]:
                        decimales_precio = int(subcampos[4])
                    if len(subcampos) > 7 and subcampos[7]:
                        decimales_medicion = int(subcampos[7])
                except (ValueError, IndexError):
                    pass

        elif tipo == 'C':
            # ~C|CODIGO|UNIDAD|RESUMEN|PRECIO1\PRECIO2\...|TIPO|
            partes = contenido.split('|')
            if len(partes) < 1:
                continue
            codigo = partes[0].strip()
            if not codigo:
                continue
            unidad = partes[1].strip() if len(partes) > 1 else ''
            resumen = partes[2].strip() if len(partes) > 2 else ''
            precio_raw = partes[3].strip() if len(partes) > 3 else '0'
            tipo_concepto = partes[4].strip() if len(partes) > 4 else ''

            # El precio puede tener varios separados por \, tomar el primero
            precio_str = precio_raw.split('\\')[0].replace(',', '.').strip()
            try:
                precio = round(float(precio_str), decimales_precio) if precio_str else 0.0
            except ValueError:
                precio = 0.0

            conceptos[codigo] = {
                'codigo': codigo,
                'descripcion': resumen,
                'unidad': unidad,
                'precio': precio,
                'tipo': tipo_concepto,  # % = capítulo, PA = partida alzada, etc.
            }

        elif tipo == 'D':
            # ~D|CODIGO_PADRE|CODIGO_HIJO\FACTOR\RENDIMIENTO\...|...
            partes = contenido.split('|')
            if len(partes) < 2:
                continue
            padre = partes[0].strip()
            hijos_raw = partes[1:]
            hijos = []
            for h in hijos_raw:
                if not h.strip():
                    continue
                subcampos = h.split('\\')
                hijo_cod = subcampos[0].strip()
                if not hijo_cod:
                    continue
                try:
                    rendimiento = float(subcampos[1].replace(',', '.')) if len(subcampos) > 1 and subcampos[1] else 1.0
                except ValueError:
                    rendimiento = 1.0
                hijos.append((hijo_cod, rendimiento))
            if padre:
                descomposicion[padre] = hijos

        elif tipo == 'M':
            # ~M|CODIGO|NLM\COMENTARIO\A\B\C\MEDICION\...|
            partes = contenido.split('|')
            if len(partes) < 2:
                continue
            codigo = partes[0].strip()
            lineas_med = []
            for m in partes[1:]:
                if not m.strip():
                    continue
                subcampos = m.split('\\')
                try:
                    med = float(subcampos[-1].replace(',', '.')) if subcampos[-1] else 0.0
                except ValueError:
                    med = 0.0
                comentario = subcampos[1].strip() if len(subcampos) > 1 else ''
                lineas_med.append({'comentario': comentario, 'medicion': med})
            if codigo:
                mediciones[codigo] = lineas_med

    # Construir árbol del presupuesto
    # La raíz del presupuesto es el concepto con código "##" o el primer capítulo
    raiz = None
    for cod in conceptos:
        if cod == '##' or (cod in descomposicion and not any(cod in [h for h, _ in v] for v in descomposicion.values())):
            raiz = cod
            break
    
    if raiz is None and conceptos:
        # Tomar el primer concepto como raíz
        raiz = next(iter(conceptos))

    def calcular_importe(codigo, nivel=0):
        """Calcula el importe de un concepto con sus mediciones."""
        concepto = conceptos.get(codigo, {})
        precio = concepto.get('precio', 0.0)
        
        # Buscar medición directa
        total_medicion = 0.0
        if codigo in mediciones:
            total_medicion = sum(m['medicion'] for m in mediciones[codigo])
        
        importe = round(precio * total_medicion, decimales_precio) if total_medicion else 0.0
        return importe, total_medicion

    def construir_nodo(codigo, nivel=0):
        """Construye recursivamente el nodo del árbol."""
        concepto = conceptos.get(codigo)
        if not concepto:
            return None

        hijos_codigos = descomposicion.get(codigo, [])
        
        # Es capítulo si tiene hijos que también tienen hijos (estructura jerárquica)
        # o si su tipo indica capítulo
        es_capitulo = bool(hijos_codigos) and nivel < 3

        if es_capitulo:
            hijos_nodos = []
            importe_total = 0.0
            for hijo_cod, _ in hijos_codigos:
                hijo_nodo = construir_nodo(hijo_cod, nivel + 1)
                if hijo_nodo:
                    hijos_nodos.append(hijo_nodo)
                    importe_total += hijo_nodo.get('importe_total', hijo_nodo.get('importe', 0.0))
            
            return {
                'codigo': codigo,
                'descripcion': concepto['descripcion'],
                'nivel': nivel,
                'es_capitulo': True,
                'partidas': hijos_nodos,
                'importe_total': round(importe_total, decimales_precio)
            }
        else:
            importe, medicion = calcular_importe(codigo)
            return {
                'codigo': codigo,
                'descripcion': concepto['descripcion'],
                'unidad': concepto['unidad'],
                'precio': concepto['precio'],
                'medicion': medicion,
                'importe': importe,
                'nivel': nivel,
                'es_capitulo': False
            }

    # Aplanar estructura en lista de partidas con jerarquía
    capitulos = []
    pem_total = 0.0

    if raiz and raiz in descomposicion:
        for cap_cod, _ in descomposicion[raiz]:
            nodo = construir_nodo(cap_cod, nivel=1)
            if nodo:
                capitulos.append(nodo)
                pem_total += nodo.get('importe_total', nodo.get('importe', 0.0))

    # Si no hay raíz identificada, crear estructura plana
    if not capitulos:
        for cod, concepto in conceptos.items():
            if cod in descomposicion:
                continue  # es padre, no partida terminal
            importe, medicion = calcular_importe(cod)
            if importe > 0:
                capitulos.append({
                    'codigo': cod,
                    'descripcion': concepto['descripcion'],
                    'unidad': concepto['unidad'],
                    'precio': concepto['precio'],
                    'medicion': medicion,
                    'importe': importe,
                    'nivel': 1,
                    'es_capitulo': False
                })
                pem_total += importe

    return {
        'obra': obra_nombre,
        'pem_total': round(pem_total, decimales_precio),
        'capitulos': capitulos,
        'total_conceptos': len(conceptos)
    }


def aplanar_partidas(capitulos, resultado=None, nivel=0):
    """Devuelve lista plana de todas las partidas (no capítulos) con su importe."""
    if resultado is None:
        resultado = []
    for nodo in capitulos:
        if nodo.get('es_capitulo'):
            aplanar_partidas(nodo.get('partidas', []), resultado, nivel + 1)
        else:
            resultado.append(nodo)
    return resultado


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python parse_bc3.py <archivo.bc3>", file=sys.stderr)
        sys.exit(1)
    
    try:
        resultado = parse_bc3(sys.argv[1])
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)
