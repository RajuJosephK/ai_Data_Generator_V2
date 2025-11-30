import streamlit as st
from config.settings import configure_page
from styles.custom_css import apply_custom_styles
from utils.api_client import get_openai_client, get_api_key
from components.sidebar import render_sidebar
from components.prompt_section import render_prompt_section
from components.output_section import render_output_section

# Configure page
configure_page()

# Apply custom styles
apply_custom_styles()

# Get API key and client
api_key = get_api_key()
if not api_key:
    st.warning("⚠️ API Key not found in secrets. Please enter it below:")
    api_key = st.text_input("OpenRouter API Key", type="password", help="Get your API key from openrouter.ai")
    if not api_key:
        st.info("👆 Enter your API key to continue")
        st.stop()

client = get_openai_client(api_key)

# Main app title
st.title("🤖 AI Test Data Generator")

# Render main sections
prompt, output_format = render_prompt_section()
render_output_section(client, prompt, output_format)

# Render sidebar
render_sidebar(api_key)