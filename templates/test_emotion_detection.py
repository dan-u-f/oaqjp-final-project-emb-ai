"""Pruebas unitarias de la función emotion_detector."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verifica que la emoción dominante sea la esperada para cada enunciado."""

    def test_joy(self):
        """'I am glad this happened' debe detectar alegría."""
        resultado = emotion_detector("I am glad this happened")
        self.assertEqual(resultado["dominant_emotion"], "joy")

    def test_anger(self):
        """'I am really mad about this' debe detectar rabia."""
        resultado = emotion_detector("I am really mad about this")
        self.assertEqual(resultado["dominant_emotion"], "anger")

    def test_disgust(self):
        """'I feel disgusted just hearing about this' debe detectar asco."""
        resultado = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(resultado["dominant_emotion"], "disgust")

    def test_sadness(self):
        """'I am so sad about this' debe detectar tristeza."""
        resultado = emotion_detector("I am so sad about this")
        self.assertEqual(resultado["dominant_emotion"], "sadness")

    def test_fear(self):
        """'I am really afraid that this will happen' debe detectar miedo."""
        resultado = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(resultado["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
