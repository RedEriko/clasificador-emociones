from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from pathlib import Path

# Creamos la aplicación de FastAPI
app = FastAPI()

# Cargamos el modelo
model = load_model('dev_model/Clasificador_emociones (4).h5')

# Mapeo de las etiquetas a nombres de emociones
emotion_labels = ['Enojo', 'Neutral', 'Disgusto', 'Miedo', 'Felicidad', 'Tristeza', 'Sorpresa']

# Ruta para servir el HTML principal
@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = Path('Frontend/index.html').read_text()
    return html_content

# Ruta para la predicción de emociones
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Guardamos la imagen en el directorio 'static/uploads'
    uploads_dir = Path('static/uploads')
    uploads_dir.mkdir(parents=True, exist_ok=True)
    file_path = uploads_dir / file.filename

    with open(file_path, 'wb') as buffer:
        buffer.write(await file.read())

    # Preprocesamos la imagen y hacemos la predicción
    predicted_emotion = predict_image(file_path)

    # Enviamos la respuesta con la emoción predicha y la URL de la imagen
    image_url = f"/static/uploads/{file.filename}"
    return JSONResponse({
        'prediction': predicted_emotion,
        'image_url': image_url
    })

# Función para preprocesar la imagen y hacer la predicción
def predict_image(file_path):
    # Cargamos la imagen y preprocesamos para el modelo
    img = image.load_img(file_path, target_size=(48, 48), color_mode="grayscale")
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalizar la imagen

    # Hacemos la predicción
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)

    # Obtenemos la etiqueta de la emoción
    return emotion_labels[predicted_class]

# Configuración de la carpeta estática
@app.get("/static/{file_path:path}")
async def serve_static(file_path: str):
    file_path = Path(f"static/{file_path}")
    if file_path.exists():
        return file_path.read_bytes()
    return JSONResponse({"error": "File not found"}, status_code=404)
