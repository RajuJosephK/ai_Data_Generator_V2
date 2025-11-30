import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to the app"""
    st.markdown("""
        <style>
        .main {
            background-color: #f3f4f6;
        }
        .stButton>button {
            background-color: #000000;
            color: white;
            border-radius: 0.5rem;
            padding: 0.5rem 1rem;
            font-weight: 600;
            border: none;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #333333;
            opacity: 0.9;
        }
        .output-box {
            background-color: #1a1a1a;
            color: #4ade80;
            padding: 1rem;
            border-radius: 0.5rem;
            font-family: monospace;
            min-height: 300px;
            max-height: 500px;
            overflow-y: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        h1 {
            color: #1f2937;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)