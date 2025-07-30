---
id: proyectos
title: Proyectos finales y ejemplos
sidebar_position: 3
---

# Proyectos finales y ejemplos

El último módulo del curso está dedicado al desarrollo de un proyecto grupal donde aplicarás todo lo aprendido. Aquí encontrarás ideas, requisitos y recomendaciones para tu proyecto.

## Requisitos generales

- Trabaja en equipos de **3 a 4 personas**.
- Usa `git` y GitHub para versionar tu código y documentar el progreso.
- Entrega un reporte final y prepara una presentación de **20 min** con los siguientes apartados:
  1. **Introducción** al problema elegido.
  2. **Arquitectura y código** de la solución paralela.
  3. **Resultados** cuantitativos acompañados de tablas o gráficas.
  4. **Conclusiones** y posibles líneas futuras.

## Ideas de proyectos

| Idea                              | Descripción breve                                        |
|----------------------------------|-----------------------------------------------------------|
| **Mandelbrot Deep‑Zoom**         | Renderiza el conjunto de Mandelbrot aprovechando GPUs y FFT. |
| **Benchmark de cifrado AES‑CBC** | Implementa y compara tiempos de cifrado en distintos nodos. |
| **Simulación de Ising 2D**       | Usa Gibbs sampling para estudiar fases en un modelo clásico. |
| **Scraper distribuido**          | Recopila DOIs y métricas JCR de forma paralela. |
| **Analizador de logs de SLURM**   | Procesa registros de ejecución para detectar patrones. |

Estas sugerencias son solo un punto de partida; cualquier proyecto que explore el cómputo distribuido con tu clúster es bienvenido.

## Consejos para el éxito

- Define un **Mínimo Producto Viable (MVP)** con entregables claros.
- Distribuye las tareas según las fortalezas de cada miembro del equipo.
- Integra mecanismos de **perfilado** (por ejemplo `cProfile` o `line_profiler`) para identificar cuellos de botella.
- Documenta tus hallazgos en un **notebook** y utiliza bibliotecas como Seaborn para elaborar gráficos atractivos.
