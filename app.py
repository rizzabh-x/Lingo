import streamlit as st
from gtts import gTTS
import playsound
from translate import Translator

# Functions for translation and text-to-speech
def translate_text(text, target_language='en'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    playsound.playsound(r"C:\Users\asus\Desktop\Final Minor\output.mp3")

# Main function for the Streamlit app
def main():
    # Custom page settings
    st.set_page_config(page_title="Translator & TTS App", page_icon="🌍", layout="wide")

    # Sidebar for Navigation
    st.sidebar.title("🌟 Welcome to Translator & TTS App!")
    st.sidebar.write("Translate text and convert it to audio in various languages.")
    st.sidebar.write("Select your options below:")

    # Sidebar input options
    target_language = st.sidebar.selectbox("Select Target Language", ["en", "es", "fr", "de", "hi"], index=0)
    st.sidebar.write("Supported Languages: English, Spanish, French, German, Hindi")
    
    # Main app layout with title and description
    st.markdown("<h1 style='text-align: center; color: #4a90e2;'>Text Translator & Text-to-Speech</h1>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Translate any text and convert it into audio in your preferred language!</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Input area for text
    input_text = st.text_area("Enter text for translation", "", placeholder="Type something here...", height=150)

    # Button to trigger translation and TTS
    if st.button("Translate & Convert to Audio 🎤"):
        if input_text:
            translated_text = translate_text(input_text, target_language)
            
            # Display translated text
            st.markdown("<h3 style='color: #4a90e2;'>Translated Text</h3>", unsafe_allow_html=True)
            st.success(translated_text)
            
            # Generate and play audio
            st.markdown("<h3 style='color: #4a90e2;'>Text-to-Speech Audio</h3>", unsafe_allow_html=True)
            text_to_speech(translated_text, language=target_language)
            st.audio("output.mp3", format="audio/mp3")
        else:
            st.warning("Please enter some text for translation.")

    # Footer with credits and styling
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Built with ❤️ by Rishabh Malav</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()