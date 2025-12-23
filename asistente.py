import os
import threading
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import pygame
import time

# Importamos el estado compartido
from estado import last_prediction

# Palabra clave para activar al asistente
hotword = 'nena'

def obtener_sintomas(enfermedad):
    sintomas = {
        "Covid-19": (
            "Presentas fiebre persistente, tos seca, mucho cansancio, pérdida del gusto o del olfato y dificultad para respirar."
        ),
        "Normal": (
            "No se detectan señales de infección pulmonar visibles en la imagen."
        ),
        "Neumonia viral": (
            "Podrías tener fiebre, tos (con o sin flema), dolor en el pecho al respirar, fatiga y dificultad al respirar."
        ),
        "Neumonia bacterial": (
            "Experimentas fiebre alta, escalofríos, tos con flema espesa, dolor intenso en el pecho y cansancio extremo."
        )
    }
    if enfermedad == 'Sin análisis':
        return "Todavía no hay un diagnóstico. Sube primero una imagen pulmonar para poder analizarla."
    return sintomas.get(enfermedad, f"No tengo información sobre los síntomas de {enfermedad}")

def obtener_recomendacion(enfermedad):
    recomendaciones = {
        "Covid-19": (
            "Aíslate inmediatamente y acude a un centro de salud. Evita el contacto con otras personas mientras esperas atención médica."
        ),
        "Normal": (
            "Aunque el análisis no muestra problemas, si tienes molestias o síntomas, consulta con un médico por seguridad."
        ),
        "Neumonia viral": (
            "Busca atención médica lo antes posible. Descansa bien, mantente hidratado y sigue las indicaciones del doctor."
        ),
        "Neumonia bacterial": (
            "Es probable que necesites antibióticos. Consulta cuanto antes con un especialista en pulmones o acude a una clínica cercana."
        )
    }
    if enfermedad == 'Sin análisis':
        return "Todavía no hay un diagnóstico. Sube primero una imagen pulmonar para poder analizarla."
    return recomendaciones.get(enfermedad, "Consulta con un profesional médico para obtener más información.")

def monitorear_audio(app_url='http://localhost:8080'):
    print("🎧 [DEBUG] Iniciando asistente de voz...")
    microfono = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 [INFO] Micrófono listo. Escuchando comandos médicos...")
            while True:
                audio = microfono.listen(source)
                try:
                    trigger = microfono.recognize_google(audio, language='es-ES').lower()
                    print('🗣️ COMANDO DETECTADO:', trigger)

                    # Comandos directos (sin palabra clave)
                    if 'síntomas' in trigger:
                        ejecutar_comandos('síntomas', app_url)
                    elif 'recomendaciones' in trigger or 'recomiendo' in trigger:
                        ejecutar_comandos('recomendación', app_url)
                    else:
                        if hotword in trigger:
                            ejecutar_comandos(trigger, app_url)

                except sr.UnknownValueError:
                    print("⚠️ No entendí lo que dijiste")
                except sr.RequestError as e:
                    print(f"[ERROR] No se pudo conectar con Google: {e}")
    except Exception as e:
        print(f"[ERROR CRÍTICO] Problema al iniciar el micrófono: {e}")

def ejecutar_comandos(trigger, app_url):
    """Ejecuta acciones según el comando detectado"""
    from estado import last_prediction

    if trigger == 'síntomas':
        enfermedad = last_prediction['prediction']
        mensaje = obtener_sintomas(enfermedad)
        print("nena:", mensaje)
        crear_audio(mensaje)

    elif trigger == 'recomendación':
        enfermedad = last_prediction['prediction']
        mensaje = obtener_recomendacion(enfermedad)
        print("nena:", mensaje)
        crear_audio(mensaje)

    elif 'analiza esta imagen' in trigger or 'diagnostica' in trigger:
        mensaje = "Por favor, carga una imagen pulmonar."
        print("nena:", mensaje)
        crear_audio(mensaje)
        webbrowser.open(app_url)

    elif 'resultado' in trigger:
        enfermedad = last_prediction['prediction']
        mensaje = f"No hay resultados aún." if enfermedad == 'Sin análisis' else f"El resultado del análisis es: {enfermedad}"
        print("nena:", mensaje)
        crear_audio(mensaje)

    else:
        mensaje = trigger.replace(hotword, '').strip()
        crear_audio(f"No entendí el comando: {mensaje}")

def crear_audio(mensaje):
    path = os.path.join('audios', 'mensaje.mp3')

    if os.path.exists(path):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except:
            pass
        os.remove(path)

    tts = gTTS(mensaje, lang='es')
    tts.save(path)
    print('nena:', mensaje)
    reproducir_audio(path)

def reproducir_audio(path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"[ERROR] No se pudo reproducir el audio: {e}")

def iniciar_asistente(app_url='http://localhost:8080'):
    """Inicia el asistente en un hilo separado"""
    thread = threading.Thread(target=monitorear_audio, args=(app_url,))
    thread.daemon = True
    thread.start()