from argparse import ArgumentParser
import sys
import logging
from models.models import get_setup, run_model

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Available models
AVAILABLE_MODELS = ["deepseek", "ollama", "openrouter"]

def get_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="RagLLM CLI App",
        usage="python main.py --model MODEL DIR",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="deepseek",
        choices=AVAILABLE_MODELS,
        help=f"Specify the model to use. Available models: {', '.join(AVAILABLE_MODELS)}",
    )
    parser.add_argument("directory", type=str, help="Directory path containing documents for RAG")
    return parser

def show_environment_help():
    """Display help for required environment variables."""
    print("\nEnvironment Variable Setup Guide:")
    print("================================")
    print("DeepSeek:")
    print("  Required: DEEPSEEK_API_KEY")
    print("  Optional: DEEPSEEK_BASE_URL, DEEPSEEK_MODEL")
    print("\nOpenRouter:")
    print("  Required: OPENROUTER_API_KEY")
    print("  Optional: OPENROUTER_MODEL")
    print("\nOllama:")
    print("  Optional: OLLAMA_MODEL")
    print("\nGeneral:")
    print("  Optional: HUGGINGFACE_EMBEDDING_MODEL")
    print("\nCreate a .env file in the project root with these variables or set them in your environment.")

def main():
    args = get_parser().parse_args()
    
    # Get the setup function for the selected model
    setup_fn = get_setup(args.model)
    if setup_fn is None:
        logging.error(f"Unknown model: {args.model}. Available models: {', '.join(AVAILABLE_MODELS)}")
        return 1
    
    logging.info(f"Initializing {args.model} model...")
    
    # Call the setup function and check if it was successful
    setup_success = setup_fn()
    if not setup_success:
        logging.error(f"Failed to set up {args.model} model. Please check your configuration.")
        show_environment_help()
        return 1
    
    logging.info(f"Successfully set up {args.model} model")
    logging.info(f"Loading documents from directory: {args.directory}")
    
    # Run the model with the given directory
    try:
        # We don't need to pass the setup function since it's already been called
        run_model(args.directory)
    except Exception as e:
        logging.error(f"Error during execution: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
