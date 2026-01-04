import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Generate text
response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="What is the capital of India?"
)

print(response.text)
