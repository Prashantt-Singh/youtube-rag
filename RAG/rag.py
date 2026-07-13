from RAG.utils import get_video_id
from RAG.transcript import get_transcript
from RAG.embedding import load_embedding_model
from RAG.vector_store import (
    create_documents,
    split_documents,
    create_vector_store,
    save_vector_store,
    load_vector_store,
    retrieve_documents
)
from RAG.llm import load_llm
from RAG.prompt import prompt
from langchain_core.output_parsers import StrOutputParser



def create_rag(url):
    #Create and save a FAISS vector store from a YouTube video.
    

    video_id = get_video_id(url)

    transcript, language = get_transcript(video_id)

    documents = create_documents(transcript)

    chunks = split_documents(documents)

    embedding_model = load_embedding_model()

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    save_vector_store(vector_store)

def format_timestamp(seconds):


    minutes = int(seconds // 60)
    seconds = int(seconds % 60)

    return f"{minutes:02d}:{seconds:02d}"

def ask_question(query):
    """Answer a user's question using the saved FAISS vector store."""

    embedding_model = load_embedding_model()

    vector_store = load_vector_store(embedding_model)

    results = retrieve_documents(
        vector_store,
        query
    )

    context = "\n\n".join(
        doc.page_content for doc, score in results
    )

    timestamp = format_timestamp(
        results[0][0].metadata["start"]
    )

    llm = load_llm()

    parser = StrOutputParser()

    chain = prompt | llm | parser

    answer = chain.invoke(
        {
            "context": context,
            "question": query
        }
    )

    return {
        "answer": answer,
        "timestamp": timestamp
    }

