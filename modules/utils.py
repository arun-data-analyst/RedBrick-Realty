import pandas as pd

# 🧪 Sample demo listings
sample_data = pd.DataFrame([
    {
        "MLS_ID": 100001,
        "Property_Type": "Condo",
        "Price": 899000,
        "Bedrooms": 2,
        "Bathrooms": 2,
        "City": "Ottawa",
        "Postal_Code": "K2P 1L4",
        "Features": "Balcony, Gym, Pool"
    },
    {
        "MLS_ID": 100002,
        "Property_Type": "Townhouse",
        "Price": 1149000,
        "Bedrooms": 3,
        "Bathrooms": 3,
        "City": "Toronto",
        "Postal_Code": "M5V 2T6",
        "Features": "Garage, Fireplace, Finished Basement"
    }
])

# ✅ Required columns list
required_columns = [
    "MLS_ID", "Property_Type", "Price", "Bedrooms", "Bathrooms",
    "City", "Postal_Code", "Features"
]
