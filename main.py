from gtts import gTTS
import playsound
from translate import Translator

def translate_text(text, target_language='en'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def text_to_speech(text, language='en', filename='output.mp3'):
    """
    Convert text to speech and play the audio.

    Parameters:
    - text (str): The text to be converted to speech.
    - language (str): The language code (default is 'en' for English).
    - filename (str): The name of the output audio file (default is 'output.mp3').
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    playsound.playsound(filename)

if __name__ == "__main__":
    # Get input text from the user
    input_text = input("Enter the text to translate: ")

    # Get the target language from the user
    target_language = input("Enter the target language: ")

    # Perform translation
    translated_text = translate_text(input_text, target_language)

    # Display the results
    print(f"\nOriginal Text: {input_text}")
    print(f"Translated Text ({target_language}): {translated_text}")

    # Convert translated text to speech
    text_to_speech(translated_text)
