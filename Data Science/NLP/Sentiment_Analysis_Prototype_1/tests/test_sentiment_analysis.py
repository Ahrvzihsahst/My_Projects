import unittest
from src.analyze_sentiment import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_positive_sentiment(self):
        result = analyze_sentiment("I love this product!")
        self.assertEqual(result, 'Positive')

    def test_negative_sentiment(self):
        result = analyze_sentiment("This is terrible!")
        self.assertEqual(result, 'Negative')

    def test_neutral_sentiment(self):
        result = analyze_sentiment("The weather is okay.")
        self.assertEqual(result, 'Neutral')

if __name__ == '__main__':
    unittest.main()
