
# ==========================================
# 1. IMPORTS AND API CONFIGURATION
# ==========================================

import os
import csv

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser


# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)


# ==========================================
# 2. SYSTEM PROMPT
# ==========================================

SYSTEM = """
ROLE:
You are the friendly assistant for Sweet Crumbs Home Bakery.

FACTS:
- Plum cake costs Rs 500.
- Chocolate cake costs Rs 650.
- Cupcakes cost Rs 80 each.
- Orders require 24 hours' notice.
- All cakes have eggless versions.

RULES:
1. Never promise a delivery time or location.
2. If the requested information is unavailable
   in the provided facts, say:
   "I'll check with the owner."
3. Calculate order totals carefully.
4. Respond in fewer than 50 words.
5. Use friendly language.
6. Support English and Telugu.
7. Match the customer's language.
"""


# ==========================================
# 3. PROMPT TEMPLATE
# ==========================================

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])


# ==========================================
# 4. CREATE LANGCHAIN PIPELINE
# ==========================================

chain = prompt | llm | StrOutputParser()


# ==========================================
# 5. CONVERSATION MEMORY
# ==========================================

history = []


def ask(question: str) -> str:

    answer = chain.invoke({
        "history": history,
        "question": question
    })

    # Store user question and assistant response
    history.extend([
        ("human", question),
        ("ai", answer)
    ])

    return answer


# ==========================================
# 6. CSV-BASED TESTING
# ==========================================

def run_tests(path: str = "tests.csv") -> None:

    with open(path, "r", encoding="utf-8") as file:

        rows = list(csv.DictReader(file))

    passed = 0

    for row in rows:

        # Independent test without conversation history
        answer = chain.invoke({
            "history": [],
            "question": row["question"]
        })

        ok = row["must_include"].lower() in answer.lower()

        if ok:
            passed += 1

        print(
            "PASS" if ok else "FAIL",
            "|",
            row["question"],
            "->",
            answer[:70]
        )

    total = len(rows)

    percentage = (passed / total * 100) if total else 0

    print(f"\n{passed}/{total} passed ({percentage:.0f}%)")


# ==========================================
# 7. MAIN CHATBOT
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print("       SWEET CRUMBS HOME BAKERY")
    print("=" * 50)

    print("Welcome! How can I help you today?")
    print("Type 'quit' to exit.")
    print("Type 'test' to run CSV-based tests.\n")

    while True:

        user_input = input("Customer: ").strip()

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nAssistant: Thank you for visiting Sweet Crumbs!")
            break

        if not user_input:
            continue

        if user_input.lower() == "test":
            run_tests()
            continue

        try:

            answer = ask(user_input)

            print("\nAssistant:", answer)
            print("\n" + "-" * 50 + "\n")

        except Exception as e:

            print("\nError:", str(e))
