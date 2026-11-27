# Task 4: Sweet Crumbs Home Bakery – AI Chatbot Using LangChain

## Task Description

Develop an AI-powered customer assistance chatbot for Sweet Crumbs Home Bakery using LangChain and the Groq API.

The chatbot helps customers obtain information about bakery products, prices, eggless cake availability, and order requirements. It uses conversational memory to maintain context across multiple interactions and supports automated response validation through CSV-based testing.

## Implementation

- Integrated the Groq API with LangChain using the `ChatGroq` class.
- Configured the `openai/gpt-oss-20b` model with a temperature of 0.3.
- Loaded API credentials securely using environment variables.
- Designed a system prompt defining the chatbot's role, bakery information, response rules, and communication style.
- Used `ChatPromptTemplate` to structure system instructions, conversation history, and customer queries.
- Implemented `MessagesPlaceholder` to dynamically include previous conversation messages.
- Created a LangChain processing pipeline using the prompt template, LLM, and `StrOutputParser`.
- Implemented conversational memory using a Python list to retain customer queries and assistant responses.
- Developed an `ask()` function to process customer questions and maintain conversation history.
- Implemented CSV-based automated testing using Python's `csv` module to validate whether generated responses contain expected keywords.
- Used independent conversation contexts for each test case to prevent previous interactions from influencing test results.
- Used `pathlib` and `__file__` to locate the test CSV file relative to the Python script, ensuring reliable file access regardless of the execution directory.

## Key Concepts Implemented

- LangChain Framework
- Groq API Integration
- Large Language Models (LLMs)
- Prompt Engineering
- Chat Prompt Templates
- Conversational Memory
- LangChain Expression Language (LCEL)
- Output Parsing
- CSV-Based Automated Testing
- Python File Handling and Path Management