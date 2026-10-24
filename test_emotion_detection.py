"""Pruebas unitarias de la función emotion_detector."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verifica que la emoción dominante sea la esperada para cada enunciado."""

    def test_emotion_detector(self):
        """Comprueba cinco enunciados con su emoción dominante."""
        casos = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for texto, esperada in casos:
            with self.subTest(texto=texto):
                resultado = emotion_detector(texto)
                self.assertEqual(resultado["dominant_emotion"], esperada)


if __name__ == "__main__":
    unittest.main()
