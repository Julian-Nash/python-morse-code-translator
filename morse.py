class MorseCodeTranslator:

    # International morse code (sample)
    morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
        " ": " ",
    }

    def translate_morse(self, morse, strict=True):

        """
        Translate#s morse code to english.
        Accepts:
            morse (str): A string of morse code to translate
            strict (bool): If True, parse and return morse code containing 4 spaces
        Returns:
            str: A translated string of text
        """

        if not morse:
            return "You must provide a string of text to translate"

        if "    " in morse and strict:
            return "Unable to translate morse code. Found 4 spaces in morse code string"

        translation = ""

        words = morse.split("   ")

        for morse_word in words:
            chars = morse_word.split(" ")
            for char in chars:
                for k, v in self.morse.items():
                    if char == v:
                        translation += k
            translation += " "

        return translation.rstrip()

    def translate_text(self, text):

        """
        Translates text to morse code.

        Accepts:
            text (str): A string of text to translate

        Returns:
            str: A translated string of morse code
        """

        if not text:
            return "You must provide a morse code string to translate"

        translation = ""

        for char in text:
            if char.lower() in self.morse:
                translation += self.morse[char.lower()] + " "

        return translation.rstrip()
