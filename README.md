# 🛡️ RedBrick Realty: The Gunner’s Listings

RedBrick Realty is a professional, Arsenal-themed real estate web application built with Streamlit. It allows users to explore demo property listings, upload their own CSV files, and optionally scrape live listings from Realtor.ca (experimental). The app enhances listings with GPT-powered luxury descriptions and can predict property prices using retrained models.

---

## 📌 Features

- 🎯 **Three Modes**
  - **Demo Mode**: Preview sample listings with or without GPT-enhanced descriptions
  - **Upload CSV**: Upload your own listings, generate descriptions, and get price predictions
  - **Live Scrape Mode**: Search listings on Realtor.ca using URL-based scraping *(experimental)*

- 🧠 **GPT Luxury Descriptions**
  - Powered by OpenAI GPT (via API)
  - Refined, aspirational tone with optional special features

- 📊 **Price Prediction**
  - Model retrained on user-uploaded CSV
  - Predicts price based on property type, beds, baths

- 🛡️ **Thematic Arsenal Branding**
  - Custom Emirates Stadium background (AB3.png)
  - Arsenal-style footer: _Crafted by Arun Acharya · Powered by Streamlit · Forever a Gunner_

- 💾 **Downloadable Output**
  - Download CSV with generated descriptions and predictions
  - UTF-8 encoded to avoid character glitches

- 🧱 **Modular Architecture**
  - `modules/`: main logic for scraping, training, and GPT generation
  - `utils/`: shared assets and helper functions
  - `assets/`: stadium background image

---

## 🚀 Setup & Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/arun-data-analyst/RedBrickRealty.git
   cd RedBrickRealty
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key**
   Create a `.env` file and add:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

5. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🗂️ Project Structure

```text
📦 RedBrickRealty/
├── streamlit_app.py               # ✅ Main unified app
├── assets/
│   └── AB3.png                    # Arsenal stadium background
├── modules/
│   ├── description_generator.py   # Calls GPT description API
│   ├── model_trainer.py           # Price prediction model
│   ├── realtor_scraper_url.py     # Realtor.ca URL-based scraping
│   └── utils.py                   # Sample data, column checks
├── utils/
│   └── luxury_generator.py        # OpenAI client and GPT wrapper
├── .env                           # 🔐 Your OpenAI API key (not committed)
├── .gitignore                     # Clean Git tracking
└── requirements.txt               # App dependencies
```

---

## 🏗️ Known Limitations

- Live scraping is experimental and may fail if Realtor.ca changes structure
- GPT features require a valid OpenAI API key and internet connection

---

## 💬 Acknowledgements

- Crafted by **Arun Acharya**
- Powered by **Streamlit**
- Inspired by the legacy of **Arsenal FC**

> *Forever a Gunner. Forever Data-Driven.* 🔴⚪