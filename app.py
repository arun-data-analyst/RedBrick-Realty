
import streamlit as st
import pandas as pd
import io
import re
import difflib

# Load background from base64 file
with open("bg_base64.txt", "r") as file:
    base64_img = file.read()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{base64_img}");
    background-size: cover;
    background-position: top center;
    background-attachment: fixed;
}}
</style>
"""

st.set_page_config(page_title="RedBrick Realty", layout="centered")
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1>🛡️ RedBrick Realty</h1>", unsafe_allow_html=True)

mode = st.radio("### Select Mode:", [
    "🔴 Demo Mode",
    "🌐 Live Scrape Mode (WIP)",
    "📤 Upload CSV"
], horizontal=True, key="mode_selector")

if st.session_state.get("last_mode") != mode:
    st.session_state["listings"] = []
    st.session_state["descriptions"] = []
    st.session_state["last_mode"] = mode

gpt_mode = st.sidebar.checkbox("💡 Show GPT-enhanced luxury descriptions")

def normalize_column(col):
    col = col.strip().lower().replace(" ", "_").replace(".", "_")
    col = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', col)
    col = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', col)
    return col.lower()

column_mapping = {
    "mls_id": "MLS_ID", "id": "MLS_ID", "listingid": "MLS_ID",
    "property_type": "Property_Type", "home_type": "Property_Type", "home_style": "Property_Type",
    "type": "Property_Type", "style": "Property_Type",
    "price": "Price", "price($)": "Price", "price_cad": "Price",
    "bedrooms": "Bedrooms", "no_of_beds": "Bedrooms", "beds": "Bedrooms",
    "bathrooms": "Bathrooms", "baths": "Bathrooms",
    "city": "City", "town": "City",
    "postal_code": "Postal_Code", "postalcode": "Postal_Code", "zip": "Postal_Code",
    "features": "Features", "amenities": "Features", "extras": "Features", "details": "Features",
    "property_features": "Features",
    "address": "Address", "full_address": "Address", "street_address": "Address",
    "status": "Status", "listing_status": "Status",
    "date_listed": "Date_Listed", "listing_date": "Date_Listed", "listed_on": "Date_Listed"
}

required_fields = {"MLS_ID", "Property_Type", "Price", "Bedrooms", "Bathrooms", "City", "Postal_Code", "Features"}

if mode == "🔴 Demo Mode":
    st.markdown("## 🧪 Demo Mode")
    def fetch_mock_listings():
        return [{
            "MLS_ID": "123456", "Property_Type": "Detached", "Price": 950000,
            "Bedrooms": 4, "Bathrooms": 3, "City": "Ottawa", "Postal_Code": "K1A 0B1",
            "Features": "Garage, Hardwood, Backyard", "Status": "Active",
            "Date_Listed": "2025-06-10", "Address": "123 Gunner Way"
        }]
    if st.button("🔍 Fetch Demo Listings"):
        st.session_state["listings"] = fetch_mock_listings()
        st.success("✅ Loaded 1 demo listing.")

elif mode == "🌐 Live Scrape Mode (WIP)":
    st.warning("🚧 Live scraping is under development. Please use Demo or CSV Upload.")

elif mode == "📤 Upload CSV":
    st.markdown("## 📤 Upload Your Own Listings")
    with open("redbrick_template.csv", "rb") as f:
        st.download_button("📎 Download Sample CSV Template", data=f, file_name="redbrick_template.csv")

    st.info("""📋 **Required Columns**
To generate high-quality descriptions, your CSV file must include:

""" + ", ".join(f"`{col}`" for col in required_fields))

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            original_cols = df.columns.tolist()
            normalized = [normalize_column(col) for col in original_cols]

            final_mapping = {}
            for orig, norm in zip(original_cols, normalized):
                if norm in column_mapping:
                    final_mapping[orig] = column_mapping[norm]
                else:
                    match = difflib.get_close_matches(norm, column_mapping.keys(), n=1, cutoff=0.7)
                    final_mapping[orig] = column_mapping[match[0]] if match else None

            mapped_cols = [k for k, v in final_mapping.items() if v]
            ignored_cols = [k for k, v in final_mapping.items() if not v]

            df = df[mapped_cols]
            df.columns = [final_mapping[k] for k in mapped_cols]

            if ignored_cols:
                st.warning("⚠️ Ignored columns: " + ", ".join(ignored_cols))

            missing = required_fields - set(df.columns)
            if missing:
                st.error("❌ Missing required columns: " + ", ".join(missing))
            else:
                st.session_state["listings"] = df.to_dict(orient="records")
                st.success(f"✅ Uploaded and mapped {len(df)} listings.")
        except Exception as e:
            st.error(f"❌ Upload failed: {e}")

if "listings" in st.session_state and st.session_state["listings"]:
    df = st.session_state["listings"]
    st.subheader("Available Properties")

    selected_index = st.selectbox(
        "Select a property:",
        options=list(range(len(df))),
        format_func=lambda i: f"{df[i].get('Property_Type', 'N/A')} | {df[i].get('City')} | ${df[i].get('Price')}"
    )

    selected_property = df[selected_index]
    st.json(selected_property)

    if gpt_mode:
        gpt_desc = (
            f"This exceptional {str(selected_property.get('Property_Type', '')).lower()} in {selected_property.get('City')} "
            f"offers {selected_property.get('Bedrooms')} bedrooms and {selected_property.get('Bathrooms')} bathrooms. "
            f"Enjoy premium features like {selected_property.get('Features') or 'modern finishes'} for just ${selected_property.get('Price', 0):,}."
        )
        st.text_area("GPT Description (placeholder)", gpt_desc, height=150)
    else:
        if "descriptions" not in st.session_state:
            st.session_state["descriptions"] = []

        if st.button("✨ Generate Description"):
            desc = (
                f"This exquisite {str(selected_property.get('Property_Type', '')).lower()} located in the heart of "
                f"{selected_property.get('City')} offers {selected_property.get('Bedrooms')} bedrooms, "
                f"{selected_property.get('Bathrooms')} bathrooms, and luxurious features such as "
                f"{str(selected_property.get('Features') or 'refined finishes')}."
                f"Perfect for sophisticated living at ${selected_property.get('Price', 0):,}."
            )
            st.session_state["descriptions"].append({
                "MLS_ID": selected_property.get("MLS_ID"),
                "City": selected_property.get("City"),
                "Price": selected_property.get("Price"),
                "Description": desc
            })
            st.text_area("Generated Description", desc, height=150)

        if st.session_state["descriptions"]:
            st.markdown("### 📥 Download All Descriptions")
            df_dl = pd.DataFrame(st.session_state["descriptions"])
            csv_buffer = io.StringIO()
            df_dl.to_csv(csv_buffer, index=False)
            st.download_button("📄 Download CSV", csv_buffer.getvalue(), "luxury_descriptions.csv", "text/csv")

from utils.predict import predict_price

# ⬇️ New section: Price Predictor
st.header("🔮 Real Estate Price Predictor")
st.caption(
    "💡 This tool uses a machine learning model trained on sample real estate data to estimate prices "
    "based on basic property features. For better results, you can also upload your own data to retrain the model."
)
st.subheader("📤 Optional: Upload Your Own Dataset")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"], help="Must include: Property_Type, Bedrooms, Bathrooms, City, Price")

if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)
    try:
        X = user_data[['Property_Type', 'Bedrooms', 'Bathrooms', 'City']]
        y = user_data['Price']

        from sklearn.linear_model import LinearRegression
        from sklearn.preprocessing import OneHotEncoder
        from sklearn.compose import ColumnTransformer
        from sklearn.pipeline import Pipeline
        import joblib

        preprocessor = ColumnTransformer(
            transformers=[('cat', OneHotEncoder(), ['Property_Type', 'City'])],
            remainder='passthrough'
        )

        new_model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', LinearRegression())
        ])

        new_model.fit(X, y)
        joblib.dump(new_model, 'model/price_model.pkl')
        st.success("✅ Model retrained using your uploaded data!")

    except Exception as e:
        st.error(f"⚠️ Failed to train model. Please check your file format.\n\nError: {e}")

with st.form("predict_form"):
    st.write("Enter property details to estimate price:")

    property_type = st.selectbox("Property Type", ["Detached", "Semi-Detached", "Condo", "Townhouse"])
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, step=1, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10, step=1, value=2)
    city = st.selectbox("City", ["Ottawa"])  # You can expand this later

    submitted = st.form_submit_button("Predict Price")

    if submitted:
        price = predict_price(property_type, bedrooms, bathrooms, city)
        st.success(f"🏠 Estimated Listing Price: **${price:,.2f}**")

footer = """
<style>
footer {
    visibility: hidden;
}
.footer-container {
    margin-top: 100px;
    padding: 10px 0;
    text-align: center;
    font-size: 14px;
    color: white;
}
.footer-container a {
    color: #82cfff;
    text-decoration: none;
}
</style>

<div class="footer-container">
    🛡️ Crafted by Arun Acharya · Inspired by Arsenal FC &nbsp;|&nbsp;
    <a href="https://github.com/arun-data-analyst" target="_blank">🔗 GitHub Portfolio</a> &nbsp;|&nbsp;
    ⚙️ Version: v1.4.3-patch2
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

