document.addEventListener("DOMContentLoaded", function() {
    let base64Image = "";

    // Previsualizar la imagen seleccionada
    document.getElementById("image-input").addEventListener("change", function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                document.getElementById("image-preview").src = e.target.result;
                document.getElementById("image-preview").style.display = "block";
                document.getElementById("predict-btn").style.display = "inline-block";
                base64Image = e.target.result.split(',')[1]; // Eliminar el prefijo "data:image/jpeg;base64,"
            };
            reader.readAsDataURL(file); // Leer la imagen y convertirla a base64
        }
    });

    // Enviar la imagen para la predicción
    document.getElementById("predict-btn").addEventListener("click", function() {
        // Mostrar el loader
        document.getElementById("loader").style.display = "inline-block";
        document.getElementById("result").style.display = "none";

        const formData = new FormData();
        const fileInput = document.getElementById('image-input');
        formData.append('file', fileInput.files[0]);

        fetch("http://localhost:8000/predict", {
            method: "POST",
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Error en la respuesta de la API");
            }
            return response.json();
        })
        .then(data => {
            setTimeout(() => {
                document.getElementById("prediction-result").textContent = `${data.predicted_class} (Confianza: ${data.confidence.toFixed(2)})`;
                document.getElementById("result").style.display = "block";
            }, 2000);
        })
        .catch(error => {
            setTimeout(() => {
                document.getElementById("prediction-result").textContent = `Error al realizar la predicción: ${error.message}`;
                document.getElementById("result").style.display = "block";
            }, 2000);
        })
        .finally(() => {
            setTimeout(() => {
                document.getElementById("loader").style.display = "none";
            }, 2000);
        });
    });
});
