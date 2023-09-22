## Langchain Q&A Application with GPT

### Overview
This project demonstrates how to create a Question & Answer (Q&A) application over a collection of documents using langchain and GPT. With langchain is possible to load documents into a Vector Database (VectorDB), then search parts of the documents that relates to the user's question, and give that parts as a context so a Large Language Model (LLM) can elaborate the response.

### Instalation
`pip install -r requirements.txt`

### Usage
1. `python db_build.py` --> to create the vector db and populate it with the document's embeddings
2. `python query_with_doc.py {question}` --> to make a question to the llm about the info of the documents
