from morse import MorseCodeTranslator

translator = MorseCodeTranslator()

text = "This string has been translated to morse code and back again"

# Translate text to morse code
morse = translator.translate_text(text)

# Translate morse code to text
translated_text = translator.translate_morse(morse)

print(morse)
print(translated_text)
