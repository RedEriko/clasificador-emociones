const form = document.getElementById("image-form");
const resultDiv = document.getElementById("result");
const predictionText = document.getElementById("prediction-text");
const imagePreview = document.getElementById("image-preview");

form.onsubmit = function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction) {
            resultDiv.style.display = 'block';
            predictionText.innerHTML = `Emoción detectada: <strong>${data.prediction}</strong>`;
            imagePreview.src = data.image_url;
        }
    })
    .catch(error => console.error('Error:', error));
};
