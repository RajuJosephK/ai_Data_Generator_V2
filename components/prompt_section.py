import streamlit as st
from config.settings import PRESETS

def render_prompt_section():
    """Render the prompt input section with presets"""
    
    # Create columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Prompt input
        st.subheader("Enter Prompt")
        
        # Initialize session state for prompt if not exists
        if 'current_prompt' not in st.session_state:
            st.session_state.current_prompt = ""
        
        prompt = st.text_area(
            "Prompt",
            value=st.session_state.current_prompt,
            height=150,
            placeholder="Enter your prompt here...",
            label_visibility="collapsed",
            key="prompt_input"
        )
        
        # Preset buttons
        st.write("**Quick Presets:**")
        cols = st.columns(3)
        
        for idx, (preset_name, preset_prompt) in enumerate(PRESETS.items()):
            with cols[idx]:
                if st.button(preset_name, key=f"preset_{idx}"):
                    st.session_state.current_prompt = preset_prompt
                    st.rerun()
    
    with col2:
        # Output format selection
        st.subheader("Settings")
        output_format = st.selectbox(
            "Output Format",
            ["JSON", "CSV", "Text"],
            index=0
        )
    
    return prompt, output_format