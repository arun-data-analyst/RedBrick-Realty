import joblib
import pandas as pd

# Load the saved model
model = joblib.load('model/price_model.pkl')

def predict_price(property_type, bedrooms, bathrooms, city):
    # Wrap the input into a DataFrame (same structure as training)
    input_df = pd.DataFrame([{
        'Property_Type': property_type,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'City': city
    }])

    # Make prediction
    predicted_price = model.predict(input_df)[0]

    # Return rounded result
    return round(predicted_price, 2)
