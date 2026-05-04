# Skill IdI UNE-PNE 41610

Skill de IA para cálculo asistido del Índice de Industrialización — IdI — en proyectos de edificación.

## Objetivo

Analizar presupuestos de proyectos de edificación y ayudar a identificar qué partidas pueden computar como componentes industrializados según criterios de la UNE-PNE 41610.

## Funcionalidades principales

- Cálculo del IdI del proyecto.
- Identificación de PEM total, PEM industrializado y PEM no industrializado.
- Desglose por función: estructura, envolvente, instalaciones, divisiones interiores, acabados, etc.
- Clasificación por geometría: 1D, 2D y 3D.
- Generación de informe de resultados.
- Trazabilidad de partidas consideradas industrializadas.
- Lectura y apoyo al análisis de presupuestos en formato BC3 / FIEBDC.

## Formatos de entrada

- Excel `.xlsx`
- BC3 / FIEBDC

## Archivos incluidos

- [`SKILL.md`](./SKILL.md): definición principal de la skill.
- [`checklist-validacion.md`](./checklist-validacion.md): checklist para revisión técnica del cálculo.
- [`disclaimer.md`](./disclaimer.md): limitaciones y advertencias de uso.
- [`references/README.md`](./references/README.md): notas sobre referencias normativas.
- [`scripts/parse_bc3.py`](./scripts/parse_bc3.py): script auxiliar para lectura de presupuestos BC3.

## Uso previsto

Esta skill está pensada para:

- consultores de industrialización;
- estudios de arquitectura;
- constructoras;
- promotoras;
- equipos técnicos en licitaciones públicas;
- proyectos vinculados a construcción industrializada.

## Flujo de trabajo recomendado

1. Cargar el presupuesto del proyecto.
2. Identificar el PEM total.
3. Detectar partidas potencialmente industrializadas.
4. Clasificar partidas por función y geometría.
5. Calcular el PEM industrializado.
6. Calcular el IdI.
7. Revisar partidas dudosas.
8. Validar el resultado con el consultor o técnico competente.
9. Generar informe final.

## Limitación importante

La skill no sustituye la validación profesional.

La IA propone una clasificación y un cálculo asistido, pero la validación final corresponde siempre al consultor o técnico competente.

Este repositorio no redistribuye el texto completo de la norma.

## Estado

Versión inicial beta.
