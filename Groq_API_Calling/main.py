
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Initialize Groq client
client = Groq()

# Send request to the AI model
text = input("Enter you query")
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is in simple words."
        }
    ]
)

# Extract AI response
answer = response.choices[0].message.content

print("AI Response:")
print(answer)
