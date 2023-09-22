import argparse


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=str,
        default="Que es Coronel Granada?",
        help="Enter the query to pass into the LLM",
    )
    return parser
