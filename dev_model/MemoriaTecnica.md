# Memoria Técnica

## Portada
- **Nombre del Proyecto**: Clasificador de Emociones
- **Fecha**: 13 Diciembre 2024
- **Integrantes**:
  - Juárez Millán Ángel Andrés
  - Lara Bustillos Damaris Aylin
  - Evaristo Ramírez Erik

 

![Emociones](../images/portada-el-cuidado-de-las-emociones-basicas.jpg)

## Índice
- [Portada](#portada)
- [Alcance del proyecto](#alcance-del-proyecto)
  - [Objetivo](#objetivo)
  - [Introducción](#introducción)
- [Fuentes de información y procedimientos aplicados](#fuentes-de-información-y-procedimientos-aplicados)
  - [Construcción del modelo](#construcción-del-modelo)
  - [Resultados modelo](#resultados-modelo)
  - [Pruebas sobre el modelo](#pruebas-sobre-el-modelo)
  - [Conclusiones](#conclusiones)
- [Conclusiones generales](#conclusiones-generales)
- [Anexos](#anexos)
- [Glosario](#glosario)

## Alcance del proyecto

### Objetivo
- Construir un modelo capaz de clasificar emociones comunes como alegría, tristeza, enojo, sorpresa, miedo y neutralidad.
- Evaluar el modelo en un conjunto de datos estándar y analizar su desempeño.

### Introducción
El análisis de emociones a partir de expresiones faciales ha capturado un interés creciente en los últimos años debido a sus aplicaciones prácticas y su relevancia en la interacción humano-computadora. Las emociones no solo son un componente esencial de la comunicación no verbal, sino que también pueden revelar el estado mental y los sentimientos de una persona, lo que resulta invaluable en una variedad de contextos.

Desde asistentes virtuales más empáticos hasta herramientas de diagnóstico en salud mental, el reconocimiento de emociones tiene aplicaciones que abarcan sectores como la atención al cliente, la educación, la psicología y la seguridad. Por ejemplo, en la educación, los sistemas de aprendizaje pueden adaptarse dinámicamente según las emociones del estudiante, mientras que en la atención médica, se pueden diseñar soluciones para detectar signos tempranos de depresión o ansiedad.

A pesar de estos beneficios, el desarrollo de clasificadores de emociones plantea varios desafíos. Factores como las diferencias culturales en la expresión de emociones, las variaciones en condiciones de iluminación y pose en las imágenes, así como la necesidad de equilibrar clases desproporcionadas en los conjuntos de datos, complican la tarea.

## Fuentes de información y procedimientos aplicados

 ![Datos por categoria](../images/ Screenshot 2024-12-13 at 13.41.16.png)

## Pipeline de Preparación
### 1. Crear Etiquetas 
- Clasificamos las imágenes 
 
### 2. División del Conjunto de Datos
- Los datos se dividen en entrenamiento y validación con proporciones del 80% y 20% respectivamente.

  | Conjunto         | Cantidad de Imágenes |
  |-------------------|----------------------|
  | Entrenamiento     | 2,197               |
  | Validación        | 550                 |
  

  - **Total de imágenes:** 2,747
  - **Etiquetas:**
