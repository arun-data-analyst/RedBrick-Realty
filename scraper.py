# scraper.py
import requests


# scraper.py

def fetch_realtor_listings(city="Ottawa", max_results=10):
    # Dummy property listings for offline testing
    return [
        {
            "MLS_ID": "123456",
            "Property_Type": "Detached",
            "Price": 950000,
            "Bedrooms": 4,
            "Bathrooms": 3,
            "City": "Ottawa",
            "Postal_Code": "K1A 0B1",
            "Features": "Finished basement, Double garage, Fenced yard"
        },
        {
            "MLS_ID": "789012",
            "Property_Type": "Condo",
            "Price": 575000,
            "Bedrooms": 2,
            "Bathrooms": 2,
            "City": "Ottawa",
            "Postal_Code": "K2P 2N6",
            "Features": "Balcony, Underground parking, Fitness center"
        }
    ]
