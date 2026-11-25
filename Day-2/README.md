# Task : Grama Panchayat Election Voter Assistance Chatbot

## Task Description

Develop an AI-powered chatbot using the Groq API to assist citizens with information and awareness related exclusively to Grama Panchayat elections in India.

The chatbot is designed to answer voters' queries about election procedures, voter eligibility, Sarpanch elections, Ward Members, Panchayat administration and other Grama Panchayat election-related topics while restricting unrelated conversations.

## Implementation

- Loaded API credentials securely from the `.env` file using `python-dotenv`.
- Initialized the Groq client to interact with the `openai/gpt-oss-20b` model.
- Designed a detailed **System Prompt** defining the chatbot's role, responsibilities, allowed topics and restricted topics.
- Implemented topic validation instructions to ensure that the chatbot responds only to Grama Panchayat election-related queries.
- Configured political neutrality to prevent candidate promotion or political influence.
- Implemented conversation memory using a messages list containing system, user and assistant messages.
- Maintained conversation history by passing previous messages along with every new request to the AI model.
- Configured model parameters such as temperature and maximum response tokens.
- Implemented a continuous chatbot loop to accept multiple user queries.
- Added exit commands (`quit`, `exit`, `bye`) to terminate the conversation.
- Implemented exception handling to manage API errors and remove failed user messages from conversation history.
- Designed a predefined response for questions unrelated to Grama Panchayat elections.

## Key Concepts Implemented

- Groq API Integration
- System Prompt Engineering
- Role-Based AI Behavior
- Topic Restriction and Validation
- Conversational Memory
- Chat Completion API
- Exception Handling
- Interactive CLI-Based Chatbot
