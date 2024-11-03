import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from translate import Translator

def translate_text(text, target_language='en'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    audio = AudioSegment.from_mp3(filename)
    play(audio)

def main():
    st.title("Text Translation and Text-to-Speech")
    st.title("")
    input_text = st.text_area("Enter text for translation:", "")
    target_language = st.selectbox("Select target language:", ["en", "es", "fr", "de", "hi"])
    if st.button("Translate and Convert to audio"):
        if input_text:
            translated_text = translate_text(input_text, target_language)
            st.subheader("Translated Text:")
            st.write(translated_text)
            st.subheader("Text-to-Speech:")
            text_to_speech(translated_text, language=target_language)
            st.audio("output.mp3",format="audio/mp3")

    if __name__ == "_main_":
        main()