import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model_and_predict(df):
    # Basic validation
    if 'price' not in df.columns:
        raise ValueError("CSV must contain a 'price' column.")

    # Select features (you can customize this)
    features = ['bedrooms', 'bathrooms', 'square_feet']
    for feature in features:
        if feature not in df.columns:
            raise ValueError(f"CSV must contain '{feature}' column.")

    # Drop rows with missing values in selected columns
    df = df.dropna(subset=['price'] + features)

    # Prepare X and y
    X = df[features]
    y = df['price']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on all rows
    predictions = model.predict(X)
    df['predicted_price'] = predictions

    return df[['price', 'predicted_price'] + features]
