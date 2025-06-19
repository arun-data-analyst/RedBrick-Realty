import streamlit as st
import requests
import json

st.title("📝 Smart Listing Description Generator")

# 📥 User Input Form
with st.form("description_form"):
    address = st.text_input("Property Address", "123 Example Street")
    unit = st.text_input("Unit (Optional)", "")
    listing_type = st.selectbox("Listing Type", ["sale", "rent"])
    size = st.number_input("Size", min_value=100, max_value=10000, value=1200)
    size_type = st.selectbox("Size Type", ["sqft", "sqm", "acres", "hectares"])
    property_type = st.selectbox("Property Type", ["detached", "semi", "town", "vacant", "link", "multiplex", "condo", "rural", "lakeside", "commercial", "industrial", "other"])
    beds = st.number_input("Bedrooms", min_value=0.0, step=0.5)
    baths = st.number_input("Bathrooms", min_value=0.0, step=0.5)
    parking = st.number_input("Parking Spots", min_value=0)
    language = st.selectbox("Language", ["English-CA", "French-CA", "Punjabi", "Spanish", "Mandarin", "Russian"])
    word_count = st.slider("Word Count", 50, 500, 200)
    special_features = st.multiselect("Special Features", ["Pool", "Gym", "Garden", "Fireplace", "Finished Basement", "Balcony"])

    submitted = st.form_submit_button("Generate Description")

# 🔁 On Submit: API Call
if submitted:
    st.info("Calling MappedBy API...")

    api_url = "https://api.mappedby.com/api/v2/listing-descriptions"
    payload = {
        "Address": address,
        "Unit": unit,
        "ListingType": listing_type,
        "Size": int(size),
        "SizeType": size_type,
        "PropertyType": property_type,
        "beds": beds,
        "baths": baths,
        "parking": int(parking),
        "Language": language,
        "WordCount": word_count,
        "SpecialFeatures": json.dumps(special_features)
    }

    try:
        response = requests.post(api_url, json=payload)
        data = response.json()

        if response.status_code == 200 and data.get("status") == "success":
            st.success("✅ Description Generated:")
            st.write(data["description"])
        else:
            st.error("❌ Failed to generate description")
            st.json(data)

    except Exception as e:
        st.error(f"Error: {e}")
