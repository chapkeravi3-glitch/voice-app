import streamlit as st
import edge_tts
import asyncio

# Page Configuration & Custom Styling
st.set_page_config(page_title="Pro Voice Generator", page_icon="🎙️", layout="centered")

# App Header
st.title("🎙️ प्रो AI वॉइस जनरेटर")
st.caption("एचडी न्यूरल आवाज़ों में टेक्स्ट को स्पीच में बदलें")

# Text Input
text = st.text_area("✍️ अपना टेक्स्ट यहाँ लिखें:", "नमस्ते! आपका स्वागत है। यह मेरी नई एआई आवाज़ है।", height=120)

# Controls in Columns
col1, col2 = st.columns(2)

with col1:
    lang = st.selectbox("🌐 भाषा (Language):", ["Hindi (भारत)", "English (India)", "English (US)"])

# Voice Options mapping based on language
voices_map = {
    "Hindi (भारत)": {
        "Swara (महिला - नेचुरल)": "hi-IN-SwaraNeural",
        "Madhur (पुरुष - नेचुरल)": "hi-IN-MadhurNeural"
    },
    "English (India)": {
        "Neerja (महिला - इंडियन)": "en-IN-NeerjaNeural",
        "Prabhat (पुरुष - इंडियन)": "en-IN-PrabhatNeural"
    },
    "English (US)": {
        "Aria (महिला - अमेरिकन)": "en-US-AriaNeural",
        "Guy (पुरुष - अमेरिकन)": "en-US-GuyNeural",
        "Jenny (महिला - एक्सप्रेसिव)": "en-US-JennyNeural",
        "Christopher (पुरुष - डीप)": "en-US-ChristopherNeural"
    }
}

with col2:
    selected_voice_name = st.selectbox("🗣️ आवाज़ चुनें (Voice Model):", list(voices_map[lang].keys()))

selected_voice = voices_map[lang][selected_voice_name]

# Advanced Audio Variations (Speed & Pitch)
st.subheader("⚙️ आवाज़ की सेटिंग्स (Variations)")
speed = st.slider("⚡ बोलने की गति (Speed):", min_value=-50, max_value=50, value=0, step=5, format="%d%%")
pitch = st.slider("🎵 आवाज़ का भारीपन (Pitch):", min_value=-20, max_value=20, value=0, step=2, format="%dHz")

# Convert sliders to edge-tts string format
rate_str = f"{'+' if speed >= 0 else ''}{speed}%"
pitch_str = f"{'+' if pitch >= 0 else ''}{pitch}Hz"

async def generate_speech(text_to_speak, voice_model, rate, pitch_val):
    communicate = edge_tts.Communicate(text_to_speak, voice_model, rate=rate, pitch=pitch_val)
    await communicate.save("speech.mp3")

st.markdown("---")

if st.button("📢 हाई-क्वालिटी आवाज़ बनाएं", type="primary", use_container_width=True):
    if text.strip():
        try:
            with st.spinner("HD आवाज़ तैयार हो रही है..."):
                asyncio.run(generate_speech(text, selected_voice, rate_str, pitch_str))
            
            st.success("✨ आपकी आवाज़ तैयार है!")
            st.audio("speech.mp3", format="audio/mp3")
        except Exception as e:
            st.error(f"एरर आया: {e}")
    else:
        st.warning("कृपया पहले कुछ टेक्स्ट दर्ज करें!")
