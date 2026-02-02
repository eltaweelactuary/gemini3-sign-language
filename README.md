# 🤟 Gemini 3 Sign Language Assistant

> **AI-Powered Egyptian Sign Language Translation using Gemini 3 API**
> Built for the Gemini 3 Hackathon 2026

[![Gemini 3](https://img.shields.io/badge/Powered%20by-Gemini%203-4285f4?style=for-the-badge&logo=google)](https://deepmind.google/technologies/gemini/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)

---

## 🎯 About

This application bridges the communication gap for the deaf and hard-of-hearing community in Egypt by leveraging **Google's Gemini 3 API** to translate Arabic text into detailed Egyptian Sign Language (ESL) descriptions.

### Key Features

- 🔄 **AI Translation** - Convert Arabic text to detailed sign language gesture descriptions
- 🎨 **Imagen Integration** - AI-generated visual sign language illustrations for better learning
- 💬 **Smart Assistant** - AI chatbot specialized for the deaf community.
- 🤖 **3D Digital Human (Preview)** - High-fidelity 3D avatar synthesis from text.
- 📚 **Sign Dictionary** - 30+ Egyptian sign language words with detailed visual and text guides.
- 🚨 **Emergency Features** - Quick access to emergency phrases and location sharing
- 🌐 **Bilingual** - Arabic/English support

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Cloud Service Account with Vertex AI access (Gemini 3 & Imagen enabled)

### Installation

```bash
# 1. Navigate to project folder
cd gemini3-hackathon

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your service account key
# Place your service-account-key.json in the project root

# 4. Run the application
### 🚀 Running the Apps

#### 1. Main Web Interface (Flask)
```bash
python app.py
```
Open: **http://localhost:5000**

#### 2. Advanced Digital Human Interface (Streamlit)
```bash
cd streamlit_app
streamlit run app.py
```
Open: **http://localhost:8501** (Requires `streamlit` and `mediapipe`)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Text AI Model** | Google Gemini 3 via Vertex AI |
| **Image AI Model** | Google Imagen via Vertex AI |
| **Backend** | Python Flask |
| **Authentication** | Service Account (GOOGLE_APPLICATION_CREDENTIALS) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Design** | Glassmorphism, Premium UI |


---

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application UI |
| `/api/translate` | POST | Translate text → sign language |
| `/api/chat` | POST | AI assistant chat |
| `/api/dictionary` | GET | Get sign language dictionary |
| `/api/emergency` | GET | Emergency phrases |
| `/health` | GET | Health check |

---

## 🏗️ Project Structure

```
gemini3-hackathon/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── service-account-key.json  # GCP credentials (not in repo)
├── sign_language_data.json   # Sign language dictionary
├── templates/
│   └── index.html           # Frontend UI
└── static/
    └── signs/               # Sign images (optional)
```

---

## 🎥 Demo

[Watch the demo video](#) *(to be added)*

---

## 👨‍💻 Developer

**Ahmed Eltaweel**
- AI Product Solution Architect
- M.Sc. Data Science, Cairo University

---

## 📜 License

MIT License - Built with ❤️ for the Gemini 3 Hackathon 2026
