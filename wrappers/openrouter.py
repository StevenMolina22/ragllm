from llama_index.core import Settings
from llama_index.llms.openrouter import OpenRouter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

# -- OpenRouter
HUGGINGFACE_EMBEDDING_MODEL = os.getenv(
    "HUGGINGFACE_EMBEDDING_MODEL", "BAAI/bge-small-en"
)
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "google/gemini-2.0-flash-exp:free")


def setup_openrouter() -> bool:
    """
    Setup OpenRouter model configuration with environment variable validation.

    Returns:
        bool: True if setup was successful, False otherwise
    """
    # Validate required environment variables
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

    # Check if API key is present
    if not openrouter_api_key:
        logging.error("Missing required environment variable: OPENROUTER_API_KEY")
        return False

    try:
        Settings.llm = OpenRouter(
            api_key=openrouter_api_key,
            model=OPENROUTER_MODEL,
        )
        logging.info(f"OpenRouter LLM configured successfully with model: {OPENROUTER_MODEL}")

        # Configure embedding model
        Settings.embed_model = HuggingFaceEmbedding(model_name=HUGGINGFACE_EMBEDDING_MODEL)
        logging.info(f"HuggingFace embedding model configured successfully: {HUGGINGFACE_EMBEDDING_MODEL}")

        return True
    except Exception as e:
        logging.error(f"Failed to setup OpenRouter configuration: {str(e)}")
        return False


def test_openrouter():
    """Test OpenRouter LLM functionality with a simple completion."""
    if not setup_openrouter():
        logging.error("Failed to set up OpenRouter. Please check your configuration.")
        return

    try:
        logging.info("Testing OpenRouter completion...")
        completion = OpenRouter(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            model=OPENROUTER_MODEL
        ).complete("Paul Graham is ")

        if completion:
            logging.info("OpenRouter test completion successful")
            print(f"Completion result: {completion}")
        else:
            logging.warning("OpenRouter returned empty completion")
    except Exception as e:
        logging.error(f"Error while testing OpenRouter: {str(e)}")


def main():
    test_openrouter()


if __name__ == "__main__":
    main()
