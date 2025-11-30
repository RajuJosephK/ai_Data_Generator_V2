import streamlit as st
import pandas as pd
import json
from utils.api_client import generate_content
from utils.data_processor import convert_to_csv
from config.settings import OPENAI_MODEL

def render_output_section(client, prompt, output_format):
    """Render the output section with generate button and results"""
    
    # Generate button
    if st.button("🚀 Generate", type="primary", use_container_width=True):
        if not prompt:
            st.warning("⚠️ Please enter a prompt first!")
        else:
            with st.spinner("Generating..."):
                content, error = generate_content(client, prompt, OPENAI_MODEL)
                
                if error:
                    st.error(f"❌ Error: {error}")
                else:
                    # Store in session state
                    st.session_state.generated_content = content
                    st.session_state.output_format = output_format
                    st.success("✅ Generated successfully!")
    
    # Output display
    st.markdown("---")
    st.subheader("📊 Output")
    
    if 'generated_content' in st.session_state:
        content = st.session_state.generated_content
        
        # Try to parse as JSON for table view
        is_json = False
        is_array = False
        data = None
        cleaned_content = content.strip()
        
        try:
            # Clean the content - remove markdown code blocks if present
            if cleaned_content.startswith('```json'):
                cleaned_content = cleaned_content.replace('```json', '').replace('```', '').strip()
            elif cleaned_content.startswith('```'):
                cleaned_content = cleaned_content.replace('```', '').strip()
            
            data = json.loads(cleaned_content)
            is_json = True
            is_array = isinstance(data, list) and len(data) > 0
                
        except Exception as e:
            # If JSON parsing fails, just show as text
            pass
        
        # Create tabs based on data type
        if is_array:
            # Show all three tabs if data is a JSON array
            tab1, tab2, tab3 = st.tabs(["📄 JSON", "📊 Table", "📋 CSV"])
            
            # JSON Tab
            with tab1:
                st.json(data)
                st.download_button(
                    label="📥 Download JSON",
                    data=json.dumps(data, indent=2),
                    file_name="data.json",
                    mime="application/json",
                    key="json_download"
                )
            
            # Table Tab
            with tab2:
                try:
                    df = pd.DataFrame(data)
                    st.dataframe(df, use_container_width=True, height=400)
                    st.download_button(
                        label="📥 Download as CSV",
                        data=df.to_csv(index=False).encode('utf-8'),
                        file_name="data.csv",
                        mime="text/csv",
                        key="table_download"
                    )
                except Exception as e:
                    st.error(f"Could not create table: {str(e)}")
            
            # CSV Tab
            with tab3:
                csv_content, csv_available = convert_to_csv(cleaned_content)
                if csv_available:
                    st.code(csv_content, language="text")
                    st.download_button(
                        label="📥 Download CSV",
                        data=csv_content,
                        file_name="data.csv",
                        mime="text/csv",
                        key="csv_download"
                    )
                else:
                    st.error("Could not convert to CSV format")
        
        elif is_json:
            # Show only JSON and Text tabs if it's JSON but not an array
            tab1, tab2 = st.tabs(["📄 JSON", "📝 Text"])
            
            with tab1:
                st.json(data)
                st.download_button(
                    label="📥 Download JSON",
                    data=json.dumps(data, indent=2),
                    file_name="data.json",
                    mime="application/json",
                    key="json_download"
                )
            
            with tab2:
                st.code(content, language="text")
                st.download_button(
                    label="📥 Download TXT",
                    data=content,
                    file_name="data.txt",
                    mime="text/plain",
                    key="txt_download"
                )
        
        else:
            # Show only text if not JSON
            st.code(content, language="text")
            st.download_button(
                label="📥 Download TXT",
                data=content,
                file_name="data.txt",
                mime="text/plain",
                key="txt_download_single"
            )
    
    else:
        st.info("👆 Generate data using the button above to see results here.")