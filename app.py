import streamlit as st
from RAG.rag import create_rag, ask_question

st.set_page_config(
    page_title="YouTube Study Assistant",
    page_icon="🎥",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.title("🎥 YouTube Study Assistant")

    st.subheader("About")
    st.write(
        "Ask questions from any English or Hindi YouTube video "
        "using Retrieval-Augmented Generation (RAG)."
    )

    st.subheader("Features")
    st.markdown("""
- 🌐 English & Hindi Transcript
- 🔍 FAISS Vector Store
- 🧠 Multilingual Embeddings
- 🤖 Groq LLM
- 📍 Timestamp Support
""")

    st.subheader("Tech Stack")
    st.markdown("""
- Streamlit
- LangChain
- HuggingFace
- FAISS
- Groq
""")

# ---------------- Main Content ---------------- #

col1, col2, col3 = st.columns([1, 2.8, 1])

with col2:

    st.title("🎥 YouTube Study Assistant")

    st.write(
        "Ask questions from any **English or Hindi YouTube video** using Multilingual RAG."
    )

    # ---------------- Process Video ---------------- #

    st.write("### Enter YouTube URL")

    youtube_url = st.text_input(
        "",
        label_visibility="collapsed"
    )

    if st.button("Process Video"):

        if youtube_url.strip() == "":
            st.warning("Please enter a YouTube URL.")

        else:
            try:
                with st.spinner("Processing video..."):
                    create_rag(youtube_url)

                st.success("Video processed successfully!")

            except Exception as e:
                st.error(str(e))

    st.write("")

    # ---------------- Ask Question ---------------- #

    st.write("### Ask a Question")

    question = st.text_input(
        "",
        key="question",
        label_visibility="collapsed"
    )

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:
            try:
                with st.spinner("Generating answer..."):
                    result = ask_question(question)

                st.write("## Answer")
                st.write(result["answer"])
                st.caption(f"📍 Timestamp: {result['timestamp']}")

            except Exception as e:
                st.error(str(e))