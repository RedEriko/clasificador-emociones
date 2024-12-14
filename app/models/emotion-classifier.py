import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

class EmotionClassifier:
    def __init__(self, model_path: str):
        """
        Inicializa el clasificador cargando el modelo de emociones.

        :param model_path: clasificador-emociones\clasificador\api\models\Clasificador_emociones_new.h5
        """
        self.model = tf.keras.models.load_model(model_path)

    def preprocess_image(self, image_path: str) -> np.ndarray:
        """
        Preprocesa una imagen para hacerla compatible con el modelo.

        :param image_path: Ruta del archivo de imagen.
        :return: Imagen preprocesada como un array de NumPy.
        """
        img = image.load_img(image_path, target_size=(48, 48), color_mode="grayscale")
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Añadir dimensión para el batch
        img_array /= 255.0  # Normalizar la imagen
        return img_array

    def predict(self, img_array: np.ndarray) -> dict:
        """
        Realiza una predicción en la imagen preprocesada.

        :param img_array: Imagen preprocesada como un array de NumPy.
        :return: Diccionario con el resultado de la predicción.
        """
        emotion_labels = ['Enojo', 'Neutral', 'Disgusto', 'Miedo', 'Felicidad', 'Tristeza', 'Sorpresa']
        prediction = self.model.predict(img_array)
        predicted_class = np.argmax(prediction)
        return {
            "predicted_class": emotion_labels[predicted_class],
            "confidence": round(np.max(prediction), 2)
        }