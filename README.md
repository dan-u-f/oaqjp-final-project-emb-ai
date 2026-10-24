# Detector de Emociones (Emotion Detector)

Aplicación web basada en IA que detecta las emociones de un texto
(rabia, asco, miedo, alegría y tristeza) usando la biblioteca **Watson NLP**
y la despliega con **Flask**. Proyecto final del curso de Python de IBM.

## Funcionalidades
- Función `emotion_detector` que consulta el servicio de emociones de Watson NLP
  y devuelve las puntuaciones de cada emoción y la emoción dominante.
- Paquete `EmotionDetection` importable desde cualquier módulo.
- Pruebas unitarias con `unittest`.
- Servidor web con Flask y manejo de errores para textos en blanco.
- Código verificado con análisis estático (`pylint`, 10/10 en `server.py`).

## Estructura
- `EmotionDetection/emotion_detection.py`: lógica de detección de emociones.
- `EmotionDetection/__init__.py`: convierte la carpeta en un paquete.
- `server.py`: aplicación Flask.
- `test_emotion_detection.py`: pruebas unitarias.
- `templates/` y `static/`: interfaz web.

## Cómo ejecutarlo
```bash
python3 server.py
```
Abre la aplicación en el puerto 5000 y escribe un texto para analizarlo.

## Pruebas y análisis estático
```bash
python3 -m unittest test_emotion_detection -v
pylint server.py
```

## Autor
Daniel Urrutia
