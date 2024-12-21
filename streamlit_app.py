import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Three.js Audio Visualizer", layout="wide")

st.title("Three.js Audio Visualizer in Streamlit")

st.markdown("""
This demo embeds a **Three.js** scene that reacts to audio frequency data.  
- **Note**: Some browsers block autoplay. If you don't hear sound, open the dev tools or click around to trigger audio playback.
""")

# Read the entire HTML file as a string
with open("visualizer.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Embed the HTML in the Streamlit app
# - height can be adjusted, set it to your preference
components.html(html_code, height=600, width=None, scrolling=False)
