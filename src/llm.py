"""
===========================================
        Module: Open-source LLM Setup
===========================================
"""
from dotenv import find_dotenv, load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import BaseChatModel

from config.config import cfg

# Load environment variables from .env file
load_dotenv(find_dotenv())


def build_llm() -> BaseChatModel:
    # Local CTransformers model
    llm = ChatOpenAI(model=cfg.MODEL, temperature=cfg.TEMPERATURE)
    return llm
