from langchain_huggingface import HuggingFaceEmbeddings

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def load_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        model_name=MODEL_NAME
    )

    return embedding_model