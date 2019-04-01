from morse import MorseCodeTranslator

translator = MorseCodeTranslator()

text = "Hello world! Translating text to morse code."

# Translate text to morse code
morse = translator.translate_text(text)

# Translate morse code to text
translated_text = translator.translate_morse(morse)

print(morse)
print(translated_text)
