"""
===========================================
        Module: Util functions
===========================================
"""
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chains.retrieval_qa.base import BaseRetrievalQA
from langchain.chat_models.base import BaseChatModel
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS, VectorStore

from config.config import cfg
from src.llm import build_llm
from src.prompts import qa_template


def set_qa_prompt() -> PromptTemplate:
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(
        template=qa_template, input_variables=["context", "question"]
    )
    return prompt


def build_qa_retrieval(
    llm: BaseChatModel, prompt: PromptTemplate, vectordb: VectorStore
) -> BaseRetrievalQA:
    qa_retrieval = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectordb.as_retriever(search_kwargs={"k": cfg.VECTOR_COUNT}),
        return_source_documents=cfg.RETURN_SOURCE_DOCUMENTS,
        chain_type_kwargs={"prompt": prompt},
    )
    return qa_retrieval


def load_db() -> VectorStore:
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.load_local(cfg.DB_PATH, embeddings)
    return vectordb


def build_retriever() -> BaseRetrievalQA:
    vectordb = load_db()
    llm = build_llm()
    qa_prompt = set_qa_prompt()
    retriever = build_qa_retrieval(llm, qa_prompt, vectordb)
    return retriever
