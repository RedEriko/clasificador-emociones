from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.emotion_classifier import EmotionClassifier
import os
import shutil
from pathlib import Path
from PIL import Image
from io import BytesIO

# Inicializa el clasificador
classifier = EmotionClassifier("clasificador-emociones\clasificador\api\models\Clasificador_emociones_new.h5")

# Inicializa API
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict", tags=["Reconocimiento de emociones"])
async def predict_image(file: UploadFile = File(...)):
    try:
        # Guardar la imagen temporalmente
        file_location = Path("uploads") / file.filename
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Preprocesar la imagen
        img_array = classifier.preprocess_image(str(file_location))

        # Realizar predicción
        result = classifier.predict(img_array)

        # Eliminar archivo temporal
        os.remove(file_location)

        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
