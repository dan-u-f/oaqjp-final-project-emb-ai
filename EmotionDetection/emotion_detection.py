"""Aplicación de detección de emociones basada en la biblioteca Watson NLP."""
import json

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Analiza un texto y devuelve las puntuaciones de cada emoción.

    Devuelve un diccionario con anger, disgust, fear, joy, sadness y
    dominant_emotion (la emoción con mayor puntuación). Si el servicio responde
    con código de estado 400 (por ejemplo, texto en blanco), todos los valores
    del diccionario son None.
    """
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)

    if response.status_code == 400:
        result = {emotion: None for emotion in EMOTIONS}
        result["dominant_emotion"] = None
        return result

    scores = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(scores, key=scores.get)
    return result
