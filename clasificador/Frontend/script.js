// Obtener elementos del DOM
const form = document.getElementById("image-form");
const resultDiv = document.getElementById("result");
const predictionText = document.getElementById("prediction-text");
const imagePreview = document.getElementById("image-preview");

// Evento de submit del formulario
form.onsubmit = function(event) {
    event.preventDefault();  // Evitar que el formulario se envíe de la forma tradicional

    const formData = new FormData(form);  // Crear un FormData con los datos del formulario

    // Realizar la petición POST a la API de FastAPI
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  // Obtener la respuesta en formato JSON
    .then(data => {
        if (data.prediction) {  // Si hay una predicción en la respuesta
            resultDiv.style.display = 'block';  // Mostrar el div con los resultados
            predictionText.innerHTML = `Emoción detectada: <strong>${data.prediction}</strong>`;  // Mostrar la predicción
            imagePreview.src = data.image_url;  // Establecer la URL de la imagen
        }
    })
    .catch(error => console.error('Error:', error));  // Manejo de errores
};
