from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer ONLY in English.

Use ONLY the information provided in the context.

If the answer is not present in the context, reply:
"I don't know based on the provided video."

Context:
{context}

Question:
{question}
"""
)