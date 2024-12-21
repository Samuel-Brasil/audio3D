# audio3D
A 3D Audio Visualizer Using Three.js and Streamlit

# Three.js + Streamlit Audio Visualizer

A minimal example showing how to embed a Three.js 3D audio visualizer inside a Streamlit app.  

## How It Works
- **visualizer.html**: Contains the Three.js scene, geometry, and audio logic.
- **streamlit_app.py**: Uses `st.components.v1.html` to embed the `visualizer.html` in Streamlit.

## Run Locally
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run streamlit_app.py`

## Deploy on Streamlit Cloud
1. Fork or copy this repo to your GitHub
2. Go to [https://share.streamlit.io/](https://share.streamlit.io/) and click "New app"  
3. Select your repo & branch, then set the main file to `streamlit_app.py`
4. Deploy!

Enjoy your 3D audio visualizer!
