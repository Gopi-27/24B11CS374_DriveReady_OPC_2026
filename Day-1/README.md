# Task 1: Groq API Integration

## Task Description
Integrate the Groq API with Python to interact with a Large Language Model (LLM) and generate AI responses based on user prompts.

## Implementation
- Imported `Groq` from the Groq Python SDK and `load_dotenv` from `python-dotenv`.
- Loaded environment variables from the `.env` file.
- Initialized the Groq client using the API key configured in the environment.
- Accepted a user query as input.
- Sent the prompt to the `openai/gpt-oss-20b` model using the Chat Completions API.
- Extracted the generated response from `response.choices[0].message.content`.
- Displayed the AI-generated response in the terminal.

---

# Task 2: Google Gemini API Integration

## Task Description
Integrate Google's Gemini API with Python to interact with a Gemini model and generate AI responses based on given prompts.

## Implementation
- Imported `genai` from the Google Gen AI SDK and `load_dotenv` from `python-dotenv`.
- Loaded environment variables from the `.env` file.
- Initialized the Gemini client using the configured API credentials.
- Sent a prompt to the Gemini model using the `generate_content()` method.
- Retrieved the generated response using `response.text`.
- Displayed the AI-generated response in the terminal.
