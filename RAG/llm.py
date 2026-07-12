import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def load_llm():
    #Load the Groq LLM

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    return llm