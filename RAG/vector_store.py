from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


def create_documents(transcript):

    documents = []

    for snippet in transcript:
        document = Document(
            page_content=snippet.text,
            metadata={
                "start": snippet.start
            }
        )

        documents.append(document)

    return documents

def split_documents(documents):


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
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


def retrieve_documents(vector_store, query):

    #Retrieve the most relevant documents for the user's query.
    documents = vector_store.similarity_search(
        query=query,
        k=4
    )

    return documents