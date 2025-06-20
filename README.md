# 🛡️ RedBrick Realty

> *Precision-crafted real estate listing generator, inspired by Arsenal FC — built for quality, not for copying.*

---

## ⚠️ License Notice

This project is **shared for personal inspiration and portfolio viewing only**.

**🔒 All rights reserved.**  
You are **not permitted to copy, reuse, or redistribute** any part of this codebase without explicit permission.

© Arun Acharya 2025

---

## 🎯 About the App

RedBrick Realty is a Streamlit-powered app that generates luxury-style Canadian real estate listing descriptions. It blends clean UI, Arsenal-themed branding, and GPT-style intelligence to help you turn raw property data into polished, professional text.

---

## 🚀 Features

- 🏠 Upload your own CSV listings or use a built-in demo
- ✨ Generate polished property descriptions with optional GPT enhancements
- 📄 Download results as CSV files
- 🧠 Price predictor powered by a trained regression model
- 🎨 Arsenal-inspired styling and UX
- 🌐 Live Scrape Mode *(UI ready — backend in progress)*

---

## 📤 Required CSV Columns

Your CSV must include the following columns (case-sensitive):

```
MLS_ID, Property_Type, Price, Bedrooms, Bathrooms, City, Postal_Code, Features
```

✅ A sample file is included at:  
`data/redbrick_template.csv`

---

## 🧪 Demo Mode

1. Select **Demo Mode**
2. View or edit the preloaded listing
3. Generate a description
4. Download the result

---

## 🛠️ Running Locally

To run the app on your machine:

```bash
git clone https://github.com/arun-data-analyst/RedBrick-Realty.git
cd RedBrick-Realty
pip install -r requirements.txt
streamlit run app.py
```

Make sure you have Python 3.10+ and `streamlit` installed.

---

## 📁 Project Structure

```
RedBrickRealty/
├── app.py                  # Main Streamlit app
├── README.md
├── .gitignore
├── data/                   # Sample & template CSVs
├── model/                  # Trained model + trainer script
├── utils/                  # Prediction logic
├── screenshots/            # UI snapshots
├── tests/                  # Optional test or experimental scripts
├── assets/                 # Optional base64 background assets
```

---

## 📸 Screenshots

![Upload UI](screenshots/upload_csv_ui.png)  
![Prediction UI](screenshots/price_predictor_ui.png)

---

## 📬 Contact

**Arun Acharya**  
[GitHub: arun-data-analyst](https://github.com/arun-data-analyst)

---

