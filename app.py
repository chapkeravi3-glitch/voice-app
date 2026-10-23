import streamlit as st
from gtts import gTTS


st.set_page_config(page_title="Voice Generator", page_icon="🎙️")
st.title("🎙️ मेल और फीमेल वॉइस जनरेटर")

text = st.text_area("यहाँ अपना टेक्स्ट लिखें:", "नमस्ते! आपका स्वागत है।", height=120)

gender = st.radio("आवाज़ चुनें:", ["Female (महिला)", "Male (पुरुष)"])
lang = st.selectbox("भाषा:", [("Hindi", "hi"), ("English", "en")])

lang_code = lang[1]

if st.button("📢 वॉइस बनाएं", type="primary"):
    if text.strip():
        try:
            if "Male" in gender:
                tld_val = 'co.in' if lang_code == 'hi' else 'co.uk'
                tts = gTTS(text=text, lang=lang_code, tld=tld_val, slow=False)
            else:
                tts = gTTS(text=text, lang=lang_code, slow=False)
            
            filename = "voice.mp3"
            tts.save(filename)
            
            st.success("✅ आपकी आवाज़ तैयार है!")
            st.audio(filename, format='audio/mp3')
            
            with open(filename, "rb") as f:
                st.download_button("📥 MP3 डाउनलोड करें", f, file_name="voice.mp3", mime="audio/mp3")
        except Exception as e:
            st.error(f"एरर आया: {e}")
