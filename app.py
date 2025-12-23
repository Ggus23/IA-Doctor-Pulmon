import os
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Importamos el estado compartido
from estado import last_prediction

app = Flask(__name__, template_folder='templates')

# Cargar modelo médico
try:
    model = load_model('./models/Doctor_Pulmon.keras')
except Exception as e:
    raise SystemExit(f"[ERROR] No se pudo cargar el modelo: {e}")

# Clases del modelo
class_names = ['Covid-19', 'Normal', 'Neumonia viral', 'Neumonia bacterial']

def preprocess_image(image_file):
    """Preprocesa una imagen para usarla en el modelo"""
    img = Image.open(image_file).convert('RGB')
    img = img.resize((256, 256))
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 256, 256, 3)
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    global last_prediction
    if request.method == 'POST':
        file = request.files['image']
        image_path = './static/uploaded_image.jpg'
        file.save(image_path)
        img = preprocess_image(image_path)
        prediction = model.predict(img)
        predicted_class = class_names[np.argmax(prediction)]
        last_prediction['prediction'] = predicted_class

        mensaje = f"El resultado del análisis es: {predicted_class}"
        print("DICIENDO:", mensaje)
        from asistente import crear_audio
        crear_audio(mensaje)

        return render_template('result.html', prediction=predicted_class, image_path='uploaded_image.jpg')

@app.route('/last_prediction')
def get_last_prediction():
    return jsonify(last_prediction)

if __name__ == '__main__':
    print("🎧 Iniciando asistente de voz...")

    # Iniciar el asistente en un hilo separado
    from threading import Thread
    from asistente import iniciar_asistente
    Thread(target=iniciar_asistente, kwargs={'app_url': 'http://localhost:8080'}, daemon=True).start()

    print("🌐 Iniciando servidor Flask...")
    app.run(host='0.0.0.0', port=8080)