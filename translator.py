from deep_translator import GoogleTranslator

print("===== Language Translation Tool =====")

text = input("Enter text: ")
target = input("Enter target language code (ta, hi, fr, es, de, en): ")

translated = GoogleTranslator(source='auto', target=target).translate(text)

print("\nOriginal Text:")
print(text)

print("\nTranslated Text:")
print(translated)