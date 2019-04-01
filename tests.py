import unittest
from morse import MorseCodeTranslator


class TestMorseCodeTranslator(unittest.TestCase):

    # Morse code to text
    def test_morse_to_text_no_morse(self):
        translator = MorseCodeTranslator()
        morse = ""
        expected_output = "You must provide a string of text to translate"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text(self):
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_numbers(self):
        translator = MorseCodeTranslator()
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_punctuation(self):
        translator = MorseCodeTranslator()
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        expected_output = "&'@)(:,=!.-+\"?/"
        self.assertEqual(translator.translate_morse(morse), expected_output)

    def test_morse_to_text_not_strict(self):
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(
            translator.translate_morse(morse, strict=False), expected_output
        )

    def test_morse_to_text_strict(self):
        translator = MorseCodeTranslator()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = (
            "Unable to translate morse code. Found 4 spaces in morse code string"
        )
        self.assertEqual(
            translator.translate_morse(morse, strict=True), expected_output
        )

    # Text to morse code
    def test_text_to_morse_no_text(self):
        translator = MorseCodeTranslator()
        text = ""
        expected_output = "You must provide a morse code string to translate"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_text_to_morse(self):
        translator = MorseCodeTranslator()
        text = "hello world"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_numbers_to_morse(self):
        translator = MorseCodeTranslator()
        text = "1234567890"
        expected_output = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_punctuation_to_morse(self):
        translator = MorseCodeTranslator()
        text = "&'@)(:,=!.-+\"?/"
        expected_output = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        self.assertEqual(translator.translate_text(text), expected_output)

    def test_all_to_morse(self):
        translator = MorseCodeTranslator()
        text = "Hello world.. 12 & 4 56 7+8 9 10, (this) is? 'Just' @ some <testing>!"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.. .-.-.- .-.-.-   .---- ..---   .-...   ....-   ..... -....   --... .-.-. ---..   ----.   .---- ----- --..--   -.--. - .... .. ... -.--.-   .. ... ..--..   .----. .--- ..- ... - .----.   .--.-.   ... --- -- .   - . ... - .. -. --. -.-.--"
        self.assertEqual(translator.translate_text(text), expected_output)


if __name__ == "__main__":
    unittest.main()
