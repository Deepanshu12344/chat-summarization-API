import cohere
import os
from dotenv import load_dotenv

load_dotenv()  

cohere_api_key = os.getenv("CO_API_KEY")
if not cohere_api_key:
    raise ValueError("CO_API_KEY is not set in the environment")

co = cohere.Client(cohere_api_key)

async def summarize_chat(messages: list[str]) -> str:
    chat_history = [{"role": "USER", "message": msg} for msg in messages]

    response = co.chat(
        model="command-r", 
        message="Summarize the above conversation.",
        chat_history=chat_history,
        temperature=0.3,
        max_tokens=300,
    )

    return response.text.strip()

async def analyze_conversation(messages: list[str]) -> str:
    # Convert messages to chat format for co.chat()
    chat_history = [{"role": "USER", "message": msg} for msg in messages]

    # Prompt to be sent as the final message
    analysis_prompt = (
        "Analyze the following conversation and provide:\n"
        "1. Sentiment (positive, neutral, or negative)\n"
        "2. Top 5 keywords\n"
        "3. User intent\n"
        "4. Summary of topics discussed"
    )

    # Perform chat with analysis prompt
    response = co.chat(
        model="command-r",  
        message=analysis_prompt,
        chat_history=chat_history,
        temperature=0.3,
        max_tokens=300,
    )

    return response.text.strip()
