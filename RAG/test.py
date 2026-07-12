from rag import ask_question

query = input("Ask a question: ")

documents = ask_question(query)

for i, doc in enumerate(documents, start=1):
    print(f"\n----- Document {i} -----")
    print(doc.page_content)
    print("Timestamp:", doc.metadata["start"])