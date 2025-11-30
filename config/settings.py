import streamlit as st

def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="AI Test Data Generator",
        page_icon="🤖",
        layout="wide"
    )

# API Configuration
OPENAI_BASE_URL = "https://openrouter.ai/api/v1"
OPENAI_MODEL = "openai/gpt-oss-20b"

# Preset prompts
PRESETS = {
    "Banking Customers": """Generate 20 UK banking customers with:
- name
- email
- phone
- address
- credit score
- balance
Return JSON only.""",
    
    "Healthcare Companies": """List 10 healthcare companies with revenue between $5B and $10B.
Return JSON: name, location, revenue_2024.""",
    
    "Transactions": """Generate 50 fake transactions:
- id
- timestamp
- merchant
- amount
Return JSON array."""
}