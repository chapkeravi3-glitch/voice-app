import streamlit as st
import edge_tts
import asyncio

st.set_page_config(page_title="Voice Generator", page_icon="🎙️")
st.title("🎙️ मेल और फीमेल वॉइस जनरेटर")

text = st.text_area("यहाँ अपना टेक्स्ट लिखें:", "नमस्ते, आपका स्वागत है!")

gender = st.radio("आवाज़ चुनें:", ["Female (महिला)", "Male (पुरुष)"])
lang = st.selectbox("भाषा:", ["Hindi", "English"])

# आवाज़ के वॉइस कोड्स (Microsoft Edge Voice Models)
voices = {
    "Hindi": {
        "Female (महिला)": "hi-IN-SwaraNeural",
        "Male (पुरुष)": "hi-IN-MadhurNeural"
    },
    "English": {
        "Female (महिला)": "en-IN-NeerjaNeural",
        "Male (पुरुष)": "en-IN-PrabhatNeural"
    }
}

selected_voice = voices[lang][gender]

async def generate_speech(text_to_speak, voice_model):
    communicate = edge_tts.Communicate(text_to_speak, voice_model)
    await communicate.save("speech.mp3")

if st.button("📢 वॉइस बनाएं", type="primary"):
    if text.strip():
        try:
            with st.spinner("आवाज़ बन रही है..."):
                asyncio.run(generate_speech(text, selected_voice))
            
            st.audio("speech.mp3", format="audio/mp3")
            st.success("आपकी आवाज़ तैयार है!")
        except Exception as e:
            st.error(f"एरर आया: {e}")
    else:
        st.warning("कृपया पहले कुछ टेक्स्ट लिखें!")

