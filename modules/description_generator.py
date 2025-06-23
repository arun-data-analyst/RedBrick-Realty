import random

def generate_description(row):
    templates = [
        f"{row['Bedrooms']} bed, {row['Bathrooms']} bath home listed at ${row['Price']:,} in {row['City']} — ideal for luxury living.",
        f"Experience modern living in this {row['Property_Type']} with {row['Bedrooms']} beds and {row['Bathrooms']} baths in {row['City']} for just ${row['Price']:,}.",
        f"Stylish {row['Property_Type']} in {row['City']} featuring {row['Bedrooms']} spacious bedrooms and {row['Bathrooms']} bathrooms — yours for ${row['Price']:,}!",
        f"Discover this gem in {row['City']}: {row['Bedrooms']} bed, {row['Bathrooms']} bath {row['Property_Type']} priced at ${row['Price']:,}.",
    ]
    return random.choice(templates)
