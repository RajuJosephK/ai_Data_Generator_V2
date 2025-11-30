import streamlit as st
from openai import OpenAI
from config.settings import OPENAI_BASE_URL

def get_api_key():

    import os
    print("Current working directory:", os.getcwd())
    print("Contents of .streamlit:", os.listdir(".streamlit") if os.path.exists(".streamlit") else ".streamlit folder not found")
    """Get API key from Streamlit secrets"""
    try:
        api_key = st.secrets["API_KEY"]
        if api_key:
            return api_key
        else:
            st.error("API Key is empty!")
            return None
    except KeyError:
        st.error("API Key not found in Streamlit secrets!")
        return None

def get_openai_client(api_key, base_url=None):
    """Initialize OpenAI/OpenRouter client with configurable base_url"""
    if base_url is None:
        base_url = OPENAI_BASE_URL  # fallback to settings

    print(f"Creating OpenAI client with base_url={base_url}")
    return OpenAI(    
        
        # base_url= "https://openrouter.ai/api/v1",
        base_url=base_url,
        api_key=api_key
        
        )




def generate_content(client, prompt, model):
    """Generate content using OpenAI API"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Return clean structured data only."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content, None
    except Exception as e:
        return None, str(e)