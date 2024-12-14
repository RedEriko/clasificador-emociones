# ![Logo Facultad de Ciencias](images/logoFC85.png) Proyecto - Clasificador de emociones en Rostros

## Integrantes:  

- Angel Andrés Juárez Millan
- Damaris Aylín Lara Bustillos
- Erik Evaristo Ramírez

## Entegrables:

1. [Memoria Técnica](dev_model/MemoriaTecnica.md)

## Contexto
Las emociones desempeñan un papel crucial en la comunicación humana, y su identificación automática tiene aplicaciones prácticas en campos como la atención al cliente, la educación, la salud mental y la industria del entretenimiento. Por ejemplo, los sistemas de atención al cliente pueden adaptarse en tiempo real según las emociones detectadas, o las plataformas educativas pueden personalizar contenidos basándose en el estado emocional del estudiante. Además, en psicología y medicina, el reconocimiento de emociones puede facilitar el diagnóstico y tratamiento de trastornos emocionales.

Clasificar emociones es un desafío debido a la diversidad cultural, las variaciones individuales y la influencia del contexto.

## Objetivo del Proyecto
Este proyecto tiene como objetivo construir un clasificador que identifique emociones comunes como alegría, tristeza, enojo, sorpresa, miedo, disgusto y neutralidad a partir de imágenes de rostros.

## Descripción General del Conjunto de Datos

Utilizamos varios conjuntos de datos que encontramos en la plataforma Kaggle, contienen carpetas etiquetadas en 7 categorías de emociones: felicidad, tristeza, enojo, miedo, sorpresa, disgusto y neutralidad.

- **FER-2013**
(Facial Expression Recognition 2013) es un conjunto de datos ampliamente utilizado en tareas de reconocimiento de emociones. Los datos consisten en imágenes de rostros en escala de grises de 48 x 48 píxeles. Los rostros se han registrado automáticamente de modo que el rostro esté más o menos centrado y ocupe aproximadamente la misma cantidad de espacio en cada imagen.
El conjunto de entrenamiento consta de 28,709 ejemplos y el conjunto de prueba público consta de 3,589 ejemplos.

- **Facial Emotion Recognition Dataset**
El conjunto de datos consta de imágenes que capturan a personas que muestran siete emociones distintas. Las imágenes abarcan una amplia gama de individuos, incluidos distintos géneros, etnias y grupos de edad.

- **Facial Emotion Dataset**
Este conjunto de datos consta de imágenes en escala de grises de rostros, cada uno con dimensiones de 48x48 píxeles. Las imágenes están preprocesadas para garantizar que cada rostro esté alineado centralmente y ocupe una cantidad de espacio constante. El desequilibrio de clases se ha mitigado ampliando las imágenes hasta cierto punto, aunque sigue habiendo cierto nivel de desequilibrio. Todas las imágenes están en formato .jpg y .jpeg.

- **Facial Emotion Expressions**
El conjunto de datos consta de imágenes en escala de grises de caras de 48x48 píxeles y hay siete categorías.

- **Face emotion dataset**
Conjunto de datos con imágenes en escala de grises.


## Enlaces Relevantes
- [FER-2013](https://www.kaggle.com/datasets/msambare/fer2013)
- [Facial Emotion Recognition Dataset](https://www.kaggle.com/datasets/tapakah68/facial-emotion-recognition)
- [Facial Emotion Dataset](https://www.kaggle.com/datasets/dilkushsingh/facial-emotion-dataset)
- [Facial Emotion Expressions](https://www.kaggle.com/datasets/samaneheslamifar/facial-emotion-expressions)
- [Face emotion dataset](https://www.kaggle.com/datasets/missaouimohamedamine/face-emotion-dataset)
