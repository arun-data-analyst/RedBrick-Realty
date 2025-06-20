# generator.py
import os
from openai import OpenAI

# Setup OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_luxury_description(property_data: dict, model="gpt-3.5-turbo") -> str:
    """
    Generate a luxury real estate listing description using OpenAI v1.x syntax
    """

    prompt = f"""
You are a luxury real estate copywriter. Write a high-end, elegant, and captivating listing description 
based on the following property details:

- Property Type: {property_data.get("Property_Type", "Unknown")}
- Location: {property_data.get("City", "Unknown")}, {property_data.get("Postal_Code", "")}
- Price: ${property_data.get("Price", "N/A")}
- Bedrooms: {property_data.get("Bedrooms", "N/A")}
- Bathrooms: {property_data.get("Bathrooms", "N/A")}
- Features: {property_data.get("Features", "None")}

Your tone should be refined, aspirational, and lifestyle-driven. Avoid clichés.
Write in 3–5 polished sentences.
"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating description: {str(e)}"
