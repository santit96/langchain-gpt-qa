import os
import timeit

import openai
from dotenv import find_dotenv, load_dotenv

from config.config import cfg
from src.arg_parser import get_parser
from src.retriever import build_retriever

# Load environment variables from .env file
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")


def print_answer(answer: dict, start: float, end: float) -> None:
    print(f'\nAnswer: {answer["result"]}')
    print("=" * 50)

    if cfg.RETURN_SOURCE_DOCUMENTS:
        # Process source documents
        source_docs = answer["source_documents"]
        for i, doc in enumerate(source_docs):
            print(f"\nSource Document {i+1}\n")
            print(f"Source Text: {doc.page_content}")
            print(f'Document Name: {doc.metadata["source"]}')
            print("=" * 60)

        print(f"Time to retrieve response: {end - start}")


if __name__ == "__main__":
    # Parse args
    parser = get_parser()
    args = parser.parse_args()

    start = timeit.default_timer()
    # Setup QA object
    qa_retriever = build_retriever()
    # Call retriever with query
    response = qa_retriever({"query": args.input})
    end = timeit.default_timer()

    print_answer(response, start, end)
