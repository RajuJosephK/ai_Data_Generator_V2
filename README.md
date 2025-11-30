# 🤖 AI Test Data Generator

A modern, modular Streamlit application that generates AI-powered test data with multiple viewing formats. Perfect for developers, testers, and data analysts who need realistic mock data quickly.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Architecture](#-architecture)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🎯 Core Functionality
- **AI-Powered Generation**: Uses OpenRouter API to generate realistic test data
- **Multiple Output Formats**: View data as JSON, interactive tables, or CSV
- **Preset Templates**: Quick-start with banking, healthcare, and transaction data templates
- **Smart Data Detection**: Automatically recognizes and formats JSON arrays
- **Download Options**: Export data in JSON, CSV, or TXT formats

### 🎨 User Experience
- **Tabbed Interface**: Clean, organized view with JSON, Table, and CSV tabs
- **Interactive Tables**: Sort, scroll, and explore data in table format
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Feedback**: Loading indicators and success/error messages

### 🏗️ Technical Features
- **Modular Architecture**: Clean separation of concerns for easy maintenance
- **Session State Management**: Persistent data across interactions
- **Error Handling**: Graceful error handling with helpful messages
- **Type Safety**: Well-structured data processing utilities

---

## 🎬 Demo

### Quick Start
1. Select a preset (Banking Customers, Healthcare Companies, or Transactions)
2. Click "Generate" button
3. View your data in multiple formats using tabs
4. Download in your preferred format

### Output Formats

**JSON Tab**: Pretty-printed JSON with syntax highlighting
```json
[
  {
    "name": "John Smith",
    "email": "john.smith@example.com",
    "balance": 5420.50
  }
]
```

**Table Tab**: Interactive, sortable data table

**CSV Tab**: CSV format preview with download option

---

## 📁 Project Structure

```
ai-data-generator/
│
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore patterns
├── README.md                       # This file
│
├── config/
│   ├── __init__.py                 # Package marker
│   └── settings.py                 # Configuration & presets
│
├── styles/
│   ├── __init__.py                 # Package marker
│   └── custom_css.py               # Custom CSS styles
│
├── utils/
│   ├── __init__.py                 # Package marker
│   ├── api_client.py               # OpenAI API integration
│   └── data_processor.py           # Data conversion utilities
│
├── components/
│   ├── __init__.py                 # Package marker
│   ├── prompt_section.py           # Prompt input UI component
│   ├── output_section.py           # Output display UI component
│   └── sidebar.py                  # Sidebar UI component
│
└── .streamlit/
    ├── config.toml                 # Streamlit theme configuration
    └── secrets.toml                # API keys (not committed)
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- OpenRouter API key ([Get one here](https://openrouter.ai))

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-data-generator.git
cd ai-data-generator
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Directory Structure

```bash
# Create necessary directories
mkdir -p .streamlit config styles utils components

# Create __init__.py files
touch config/__init__.py styles/__init__.py utils/__init__.py components/__init__.py
```

---

## ⚙️ Configuration

### API Key Setup

#### Local Development

Create `.streamlit/secrets.toml`:

```bash
mkdir .streamlit
```

Add your API key:

```toml
# .streamlit/secrets.toml
API_KEY = "your_openrouter_api_key_here"
```

⚠️ **Important**: Never commit `secrets.toml` to Git! It's already in `.gitignore`.

#### Environment Variables (Alternative)

You can also use a `.env` file:

```bash
# .env
API_KEY=your_openrouter_api_key_here
```

### Theme Configuration (Optional)

Edit `.streamlit/config.toml` to customize appearance:

```toml
[theme]
primaryColor = "#4ade80"
backgroundColor = "#f3f4f6"
secondaryBackgroundColor = "#ffffff"
textColor = "#1f2937"
font = "sans serif"

[server]
headless = true
port = 8501
```

### Preset Prompts

Customize presets in `config/settings.py`:

```python
PRESETS = {
    "Your Custom Preset": """Your custom prompt here..."""
}
```

---

## 💻 Usage

### Running Locally

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows

# Run the application
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Using the Application

#### 1. Enter a Prompt
- Type your own custom prompt, or
- Click one of the preset buttons

#### 2. Choose Format (Optional)
- JSON (default)
- CSV
- Text

#### 3. Generate Data
- Click the "🚀 Generate" button
- Wait for AI to generate your data

#### 4. View Results
- **JSON Tab**: View formatted JSON data
- **Table Tab**: Interactive table for arrays
- **CSV Tab**: CSV format preview

#### 5. Download
- Each tab has its own download button
- Choose your preferred format

### Example Prompts

**Banking Data:**
```
Generate 20 UK banking customers with:
- name
- email
- phone
- address
- credit score
- balance
Return JSON only.
```

**E-commerce Orders:**
```
Generate 30 fake e-commerce orders with:
- order_id
- customer_name
- product
- quantity
- price
- order_date
Return JSON array.
```

**Employee Records:**
```
Create 15 employee records with:
- employee_id
- full_name
- department
- position
- salary
- hire_date
Return JSON only.
```

---

## ☁️ Deployment

### Deploy to Streamlit Cloud

#### Step 1: Prepare Your Repository

1. **Push to GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/ai-data-generator.git
git push -u origin main
```

2. **Ensure files are ready**:
- ✅ `app.py` exists
- ✅ `requirements.txt` exists
- ✅ `.gitignore` includes `.streamlit/secrets.toml`

#### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repository
5. Set main file path: `app.py`
6. Click **"Advanced settings"**

#### Step 3: Add Secrets

In the **Secrets** section, add:

```toml
API_KEY = "your_openrouter_api_key_here"
```

#### Step 4: Deploy

1. Click **"Deploy!"**
2. Wait 2-3 minutes for deployment
3. Your app will be live at: `https://your-app-name.streamlit.app`

### Updating Your Deployed App

Simply push changes to GitHub:

```bash
git add .
git commit -m "Update feature"
git push
```

Streamlit Cloud will auto-deploy in ~1 minute!

### Other Deployment Options

- **Heroku**: Use Streamlit's Heroku buildpack
- **AWS EC2**: Run on virtual machine
- **Docker**: Containerize for any platform
- **Google Cloud**: Deploy on Cloud Run

---

## 🏛️ Architecture

### Design Principles

1. **Separation of Concerns**: Each module has a single responsibility
2. **Modularity**: Components are independent and reusable
3. **Maintainability**: Easy to update and extend
4. **Scalability**: Can grow with new features

### Module Responsibilities

#### `app.py`
- Application entry point
- Orchestrates all components
- Minimal logic, mostly imports

#### `config/settings.py`
- Application configuration
- API endpoints and models
- Preset prompt templates

#### `styles/custom_css.py`
- All CSS styling
- Theme customization
- UI appearance

#### `utils/api_client.py`
- OpenAI API integration
- Client initialization
- API key management
- Content generation

#### `utils/data_processor.py`
- Data conversion (JSON to CSV)
- Data validation
- Format transformation

#### `components/prompt_section.py`
- Prompt input interface
- Preset button handlers
- Format selection

#### `components/output_section.py`
- Generate button logic
- Tab creation and management
- Download functionality

#### `components/sidebar.py`
- Sidebar information
- API key status
- Usage instructions

### Data Flow

```
User Input → Prompt Section → API Client → OpenAI API
                                    ↓
                            Response Content
                                    ↓
                        Data Processor (Clean & Parse)
                                    ↓
                        Output Section (Display in Tabs)
                                    ↓
                            User Downloads
```

---

## 🎨 Customization

### Adding New Presets

Edit `config/settings.py`:

```python
PRESETS = {
    "Your New Preset": """
Your custom prompt here...
Make sure to specify:
- What data to generate
- Format (JSON, CSV, etc.)
- Number of records
""",
}
```

### Changing Colors

Edit `styles/custom_css.py`:

```python
def apply_custom_styles():
    st.markdown("""
        <style>
        .stButton>button {
            background-color: #YOUR_COLOR;  /* Change button color */
        }
        .output-box {
            background-color: #YOUR_COLOR;  /* Change output background */
            color: #YOUR_COLOR;             /* Change output text */
        }
        </style>
    """, unsafe_allow_html=True)
```

### Adding New Components

1. **Create new component file**:
```bash
touch components/your_component.py
```

2. **Define component**:
```python
import streamlit as st

def render_your_component():
    """Your component logic"""
    st.write("Your component content")
```

3. **Import in app.py**:
```python
from components.your_component import render_your_component

# In main app
render_your_component()
```

### Adding New Data Processors

Edit `utils/data_processor.py`:

```python
def convert_to_xml(content):
    """Convert JSON to XML format"""
    # Your conversion logic
    return xml_content
```

### Changing AI Model

Edit `config/settings.py`:

```python
OPENAI_MODEL = "anthropic/claude-3-sonnet"  # Change to any supported model
```

---

## 🐛 Troubleshooting

### Common Issues

#### Tabs Not Appearing

**Problem**: Generate button works but no tabs show

**Solution**:
1. Check if data is valid JSON array
2. Look for error messages in terminal
3. Try with a preset button first
4. Restart Streamlit: `Ctrl+C` then `streamlit run app.py`

#### API Key Errors

**Problem**: "API_KEY not found" error

**Solutions**:
1. Check `.streamlit/secrets.toml` exists
2. Verify API key is correct
3. Ensure file format is correct (TOML, not JSON)
4. Restart Streamlit app after adding key

```toml
# Correct format
API_KEY = "sk-or-v1-..."

# Wrong format
"API_KEY": "sk-or-v1-..."  # ❌ This is JSON
```

#### Module Import Errors

**Problem**: `ModuleNotFoundError: No module named 'config'`

**Solutions**:
1. Ensure `__init__.py` files exist in all folders
2. Check you're running from project root
3. Verify virtual environment is activated

```bash
# Create missing __init__.py files
touch config/__init__.py
touch styles/__init__.py
touch utils/__init__.py
touch components/__init__.py
```

#### CSV Download Not Working

**Problem**: CSV download button is disabled

**Solutions**:
1. Ensure data is a JSON array (not object)
2. Check data has consistent keys
3. Try with preset buttons first

#### Streamlit Cloud Deployment Fails

**Problem**: App crashes on Streamlit Cloud

**Solutions**:
1. Check `requirements.txt` is complete
2. Verify secrets are added in Streamlit Cloud dashboard
3. Check logs in Streamlit Cloud interface
4. Ensure Python version compatibility (use Python 3.8+)

### Debug Mode

To see detailed error information, run:

```bash
streamlit run app.py --logger.level=debug
```

### Getting Help

1. Check the [Streamlit Documentation](https://docs.streamlit.io)
2. Review [OpenRouter API Docs](https://openrouter.ai/docs)
3. Open an issue on GitHub
4. Contact the maintainer

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs

1. Check if bug already exists in Issues
2. Create new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

### Suggesting Features

1. Open a feature request issue
2. Describe the feature clearly
3. Explain use case and benefits

### Pull Requests

1. Fork the repository
2. Create feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Open Pull Request

### Development Setup

```bash
# Fork and clone
git clone https://github.com/yourusername/ai-data-generator.git
cd ai-data-generator

# Create branch
git checkout -b feature/your-feature

# Make changes and test
streamlit run app.py

# Commit and push
git add .
git commit -m "Your descriptive message"
git push origin feature/your-feature
```

---


## 🙏 Acknowledgments

- **Streamlit** - For the amazing framework
- **OpenRouter** - For API access to multiple AI models
- **OpenAI** - For powerful language models
- **Pandas** - For data manipulation

---

## 📊 Project Stats

- **Language**: Python 3.8+
- **Framework**: Streamlit 1.28.0
- **API**: OpenRouter
- **Lines of Code**: ~500
- **Modules**: 8
- **Components**: 3

---

## 🗺️ Roadmap

### Current Features ✅
- AI-powered data generation
- Multiple output formats
- Preset templates
- Download functionality

### Planned Features 🚧
- [ ] User authentication
- [ ] Save/load prompt history
- [ ] Custom data schemas
- [ ] Bulk generation
- [ ] API rate limiting display
- [ ] More preset templates
- [ ] Data validation rules
- [ ] Export to databases
- [ ] Scheduling/automation
- [ ] Team collaboration

---

## 📞 Contact

- **Author**: Raju Joseph K
- **GitHub**: [@RajuJosephk](https://github.com/RajuJosephK)


---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐️ on GitHub!

---

**Made with ❤️ and Streamlit**