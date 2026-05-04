# Skill: Cálculo asistido del IdI según UNE-PNE 41610

## Objetivo

Calcular de forma asistida el Índice de Industrialización — IdI — de un proyecto de edificación a partir de su presupuesto.

## Inputs necesarios

- Presupuesto del proyecto en formato `.xlsx` o `.bc3`.
- PEM total.
- Partidas del presupuesto.
- Descripciones de unidades de obra.
- Importes por partida.
- Criterios de clasificación del consultor.

## Procedimiento

1. Leer el presupuesto.
2. Identificar partidas potencialmente industrializadas.
3. Excluir partidas que no cumplan la definición aplicable de componente industrializado.
4. Clasificar las partidas válidas por función.
5. Clasificar las partidas válidas por geometría: 1D, 2D o 3D.
6. Calcular el PEM industrializado.
7. Calcular el IdI.
8. Generar resumen ejecutivo.
9. Generar detalle revisable por partida.
10. Señalar partidas dudosas para validación del consultor.

## Outputs esperados

- PEM total.
- PEM industrializado.
- PEM no industrializado.
- Índice de Industrialización — IdI.
- Desglose por función.
- Desglose por geometría.
- Tabla de partidas industrializadas.
- Justificación preliminar por partida.
- Advertencias de validación.

## Criterios de calidad

- No computar partidas sin justificación.
- No asumir que un producto es industrializado solo por estar prefabricado parcialmente.
- Separar partidas claramente válidas, dudosas y excluidas.
- Mantener trazabilidad del cálculo.
- Indicar siempre que la validación final corresponde al técnico competente.

## Limitaciones

Esta skill no interpreta de forma vinculante la norma, no sustituye la revisión contractual y no reemplaza la validación profesional del consultor.
