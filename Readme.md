# 🫁 Doctor Pulmon IA
Sistema inteligente de apoyo al diagnóstico pulmonar mediante Deep Learning y asistencia por voz.

Este proyecto implementa un modelo de **Deep Learning con TensorFlow/Keras** capaz de analizar imágenes médicas de tórax y clasificar posibles patologías pulmonares.  
La aplicación está desarrollada con **Flask** y cuenta con un **asistente de voz** que comunica el resultado del análisis al usuario.

> ⚠️ Proyecto con fines **educativos, académicos y demostrativos**.  
> No reemplaza el diagnóstico de un profesional de la salud.

---

## 🎯 Objetivo del Proyecto

Desarrollar un sistema funcional que permita:

- Analizar imágenes de rayos X de tórax
- Clasificar enfermedades pulmonares comunes
- Mostrar resultados de forma visual
- Comunicar el diagnóstico mediante audio (Text-to-Speech)
- Demostrar un flujo completo de IA aplicada (modelo + backend + interfaz)

---

## 🧠 Patologías Detectadas

El modelo clasifica las imágenes en las siguientes categorías:

- **Covid-19**
- **Normal**
- **Neumonía viral**
- **Neumonía bacterial**

---

## 🏗️ Arquitectura del Proyecto
├── app.py # Servidor Flask principal
├── asistente.py # Asistente de voz (Text-to-Speech)
├── estado.py # Estado compartido de la predicción
├── models/
│ └── Doctor_Pulmon.keras # Modelo entrenado (incluido)
├── templates/
│ ├── index.html # Página principal
│ └── result.html # Resultado del diagnóstico
├── static/
│ └── uploaded_image.jpg # Imagen cargada en tiempo de ejecución
├── requirements.txt # Dependencias del proyecto
└── README.md
---

## ⚙️ Tecnologías Utilizadas

- **Python 3.10+**
- **Flask**
- **TensorFlow / Keras**
- **NumPy**
- **Pillow (PIL)**
- **HTML / CSS**
- **Text-to-Speech (asistente de voz)**

---

## 🧠 Modelo Entrenado (Incluido)

Este repositorio **incluye el modelo entrenado** `Doctor_Pulmon.keras` con el objetivo de:

- Permitir la **ejecución inmediata** del sistema
- Mostrar un proyecto **completamente funcional**
- Evidenciar el trabajo realizado en entrenamiento y despliegue del modelo

El modelo fue entrenado previamente y se distribuye **exclusivamente con fines educativos y demostrativos**.

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/doctor-pulmon-ia.git
cd doctor-pulmon-ia
2️⃣ Crear entorno virtual (recomendado)
bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
3️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
4️⃣ Ejecutar la aplicación
bash
Copiar código
python app.py
La aplicación estará disponible en:

arduino
Copiar código
http://localhost:8080
🔊 Asistente de Voz
El sistema incorpora un asistente que reproduce por audio el resultado del diagnóstico.

Se ejecuta en un hilo independiente al iniciar la aplicación.

Convierte automáticamente el texto del resultado en voz.

⚠️ Aviso Legal
Este proyecto:

❌ No reemplaza diagnóstico médico profesional

✔️ Es un sistema de apoyo educativo y experimental

✔️ Está orientado a demostración de IA aplicada a la salud

📌 Posibles Mejoras Futuras
Historial de diagnósticos

Soporte para múltiples imágenes

Panel administrativo

Autenticación de usuarios

Explicabilidad del modelo (Grad-CAM)

Despliegue en la nube

👨‍💻 Autor
Agustín Pacar
Proyecto académico de Inteligencia Artificial aplicada a la salud.