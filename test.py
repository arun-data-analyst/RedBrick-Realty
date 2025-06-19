# test.py
import os
from openai import OpenAI

# Load API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Test chat completion call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello, who are you?"}
    ],
    temperature=0.5
)

print(response.choices[0].message.content)


