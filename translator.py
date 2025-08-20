from googletrans import Translator
import streamlit as st

st.title("🌐 Language Translation Tool")

text = st.text_area("✏️ Enter text to translate:")

languages = {
    'English': 'en',
    'Hindi': 'hi',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es',
    'Japanese': 'ja',
    'Chinese': 'zh-cn'
}

source_lang = st.selectbox("🔤 Source Language", list(languages.keys()))
target_lang = st.selectbox("🌍 Target Language", list(languages.keys()))

if st.button("🔁 Translate"):
    if text:
        translator = Translator()
        translated = translator.translate(text, src=languages[source_lang], dest=languages[target_lang])
        st.success(f"📝 Translated Text:\n{translated.text}")
    else:
        st.warning("⚠️ Please enter some text to translate.")
