'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain.chat_models import ChatOpenAI
from dotenv import find_dotenv, load_dotenv
import box
import yaml

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Import config vars
with open('config/config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


def build_llm():
    # Local CTransformers model
    llm = ChatOpenAI(
        model=cfg.MODEL,
        temperature=cfg.TEMPERATURE
    )
    return llm
