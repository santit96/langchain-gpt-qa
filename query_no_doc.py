from src.llm import build_llm
from src.arg_parser import get_parser

parser = get_parser()
args = parser.parse_args()
llm = build_llm()
prediction = llm.predict(args.input)
print(prediction)
