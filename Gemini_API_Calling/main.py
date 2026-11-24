from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Create Gemini client
client = genai.Client()

# Send request to Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain what an API is in simple words."
)

# Extract and print response
print("\nGemini Response:")
print(response.text)