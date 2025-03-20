from argparse import ArgumentParser
from models import run_ollama, run_deepseek
import argparse

def get_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser(
        description="My CLI App",
        usage="my_app --model MODEL --env ENV DIR"  # Custom usage message
    )
    parser.add_argument(
        "--model",
        type=str,
        default="deepseek",
        help="Specify the model to use (e.g., deepseek)"  # Help text
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Directory path"
    )
    return parser

def main():
    args = get_parser().parse_args()

    match args.model:
        case "deepseek":
            run_deepseek(args.directory)
        case "ollama":
            run_ollama(args.directory)
        case _:
            print("Not a valid model.")

if __name__ == "__main__":
    main()
