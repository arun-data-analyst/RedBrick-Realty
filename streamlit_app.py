# streamlit_app.py — Final Version with Working Background and WIP Notice

import streamlit as st
import pandas as pd
from io import StringIO
from modules.description_generator import generate_description
from modules.realtor_scraper_url import scrape_realtor_url
from modules.model_trainer import train_model_and_predict
from utils.luxury_generator import sample_data, required_columns
import base64

# ✅ Arsenal-themed background function
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

def set_background(image_path: str):
    encoded_img = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{encoded_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 🚀 Configure Page
st.set_page_config(
    page_title="RedBrick Realty: The Gunner’s Listings",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🏡",
)

set_background("assets/AB3.png")

# Sidebar controls
st.sidebar.header("🔘 Mode Selection")
mode = st.sidebar.radio("Select Mode:", ["Demo Mode", "Live Scrape Mode (WIP)", "Upload CSV"])
use_gpt = st.sidebar.checkbox("💡 Show GPT-enhanced luxury descriptions")

# Main Title
st.markdown("""<h1 style='text-align: center;'>🛡️ RedBrick Realty</h1>""", unsafe_allow_html=True)

# === DEMO MODE ===
if mode == "Demo Mode":
    st.subheader("🏠 Sample Listings")
    df = sample_data.copy()
    if use_gpt:
        df["Description"] = df.apply(generate_description, axis=1)
    st.dataframe(df)

# === LIVE SCRAPE MODE ===
elif mode == "Live Scrape Mode (WIP)":
    st.subheader("🌐 Live Scrape from Realtor.ca")
    st.markdown("<i>Note: This feature is still under development. Results may be limited or incomplete.</i>", unsafe_allow_html=True)

    neighborhood = st.text_input("Enter Ottawa Neighborhood", "Barrhaven")
    transaction_type = st.selectbox("Transaction Type", ["sale", "rent", "sold"])
    min_price = st.selectbox("Min Price", ["0", "1000", "1600", "2000", "3000"])
    max_price = st.selectbox("Max Price", ["2000", "3000", "4000", "5000"])
    min_beds = st.selectbox("Min Beds", ["1", "2", "3", "4"])
    min_baths = st.selectbox("Min Baths", ["1", "2", "3", "4"])

    if st.button("🔎 Scrape Listings"):
        with st.spinner("Scraping Realtor.ca listings..."):
            listings = scrape_realtor_url(
                neighborhood, transaction_type, min_price, max_price, min_beds, min_baths
            )
            df = pd.DataFrame(listings)
            if df.empty:
                st.warning("No listings found.")
            else:
                if use_gpt:
                    df["Description"] = df.apply(generate_description, axis=1)
                st.success(f"✅ Scraped {len(df)} listings")
                st.dataframe(df)

# === UPLOAD CSV ===
elif mode == "Upload CSV":
    st.subheader("📂 Upload Your Own Listings")
    st.download_button("📅 Download Sample CSV Template", sample_data.to_csv(index=False),
                       file_name="sample_real_estate_template.csv")

    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully.")
        st.write("### Preview of Listings:")
        st.dataframe(df)

        if all(col in df.columns for col in required_columns):
            if use_gpt:
                df["Description"] = df.apply(generate_description, axis=1)

            st.subheader("🔮 Real Estate Price Predictor")
            retrained_df = df.dropna(subset=["Price", "Bedrooms", "Bathrooms", "Property_Type"])
            st.success("Model retrained using your uploaded data!")

            selected_type = st.selectbox("Property Type", retrained_df["Property_Type"].unique())
            selected_beds = st.number_input("Bedrooms", 1, 10, step=1)
            selected_baths = st.number_input("Bathrooms", 1, 10, step=1)

            if st.button("📊 Predict Price"):
                prediction = train_model_and_predict(retrained_df, selected_type, selected_beds, selected_baths)
                st.info(f"Estimated Price: ${int(prediction):,}")

            csv_with_encoding = df.to_csv(index=False, encoding="utf-8-sig")
            st.download_button("⬇️ Download Listings with Descriptions", csv_with_encoding,
                               file_name="generated_descriptions.csv", mime="text/csv")
        else:
            st.error(f"Missing required columns: {', '.join(required_columns)}")

# Footer
st.markdown(
    """
    <hr style='margin-top: 3rem; margin-bottom: 1rem;'>
    <div style='text-align: center; font-size: 14px; color: #888;'>
        Crafted by Arun Acharya · Powered by Streamlit · Forever a Gunner
    </div>
    """,
    unsafe_allow_html=True
)
