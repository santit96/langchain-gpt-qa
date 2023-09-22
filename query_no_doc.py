from src.arg_parser import get_parser
from src.llm import build_llm

parser = get_parser()
args = parser.parse_args()
llm = build_llm()
prediction = llm.predict(args.input)
print(prediction)
