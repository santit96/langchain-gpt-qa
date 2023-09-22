# =========================
#  Module: Vector DB Build
# =========================
import os

import openai
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

from config.config import cfg

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Build vector database
def run_db_build() -> None:
    # Load document
    loader = DirectoryLoader(cfg.DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Transform document
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=cfg.CHUNK_SIZE, chunk_overlap=cfg.CHUNK_OVERLAP
    )
    texts = text_splitter.split_documents(documents)

    # Get embeddings
    embeddings = OpenAIEmbeddings()

    # Save in vector db
    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local(cfg.DB_PATH)


if __name__ == "__main__":
    run_db_build()
