from translator import english_to_french, french_to_english
import unittest


class TestTranslator(unittest.TestCase):

    '''tests for null input'''
    def test_null(self):
        self.assertEqual(english_to_french(), '', 'null')
        self.assertEqual(french_to_english(), '', 'null')

    '''tests English to French'''
    def test_english(self):
        self.assertNotEqual(english_to_french(None), 'Bonjour')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    '''tests French to English'''
    def test_frenchToEnglish(self):
        self.assertNotEqual(french_to_english(None), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
    