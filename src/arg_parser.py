import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input',
                        type=str,
                        default='Hi!',
                        help='Enter the query to pass into the LLM')
    return parser
