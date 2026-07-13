from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


def create_documents(transcript, chunk_duration=40):
    documents = []
    block = []
    start_time = transcript[0].start if transcript else None

    for snippet in transcript:
        if start_time is None:
            start_time = snippet.start

        block.append(snippet.text)

        if snippet.start - start_time >= chunk_duration:
            documents.append(Document(
                page_content=" ".join(block),
                metadata={"start": start_time}
            ))
            block = []
            start_time = None

    if block:
        documents.append(Document(
            page_content=" ".join(block),
            metadata={"start": start_time}
        ))

    return documents

def split_documents(documents):


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=300
    )

    chunks = text_splitter.split_documents(documents)

    return chunks

def create_vector_store(chunks, embedding_model):


    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store

def save_vector_store(vector_store):
    
    #Save the FAISS vector store locally.


    vector_store.save_local("Vectorstore/faiss_index")

def load_vector_store(embedding_model):

    #Load the saved FAISS vector store.
    

    vector_store = FAISS.load_local(
        "Vectorstore/faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store


def retrieve_documents(vector_store, query, k=8):
    results = vector_store.similarity_search_with_score(query=query, k=k)
    return results  