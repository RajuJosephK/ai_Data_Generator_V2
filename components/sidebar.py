import streamlit as st

def render_sidebar(api_key):
    """Render the sidebar with information"""
    
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This tool generates AI-powered test data for various use cases.
        
        **How to use:**
        1. Enter a prompt or click a preset
        2. Choose output format
        3. Click Generate
        4. Download your data
        
        **Supported Formats:**
        - JSON
        - CSV (for array data)
        - Plain Text
        """)
        
        st.markdown("---")
        st.markdown("**Powered by:**")
        st.markdown("- OpenRouter AI")
        st.markdown("- Streamlit")
        
        st.markdown("---")
        
        # API Key status
        if api_key:
            st.success("✅ API Key Loaded")
        else:
            st.error("❌ API Key Missing")
