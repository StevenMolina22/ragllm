from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

# -- Ollama
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")


def setup_ollama() -> bool:
    """
    Setup Ollama model configuration with environment variable validation.

    Returns:
        bool: True if setup was successful, False otherwise
    """
    try:
        Settings.llm = Ollama(model=OLLAMA_MODEL, request_timeout=420)
        Settings.embed_model = OllamaEmbedding(model_name=OLLAMA_MODEL)
        logging.info(f"Ollama LLM configured successfully with model: {OLLAMA_MODEL}")
        return True
    except Exception as e:
        logging.error(f"Failed to setup Ollama configuration: {str(e)}")
        return False


def test_ollama():
    """Test Ollama LLM functionality with a simple completion."""
    if not setup_ollama():
        logging.error("Failed to set up Ollama. Please check your configuration.")
        return

    try:
        logging.info("Testing Ollama completion...")
        completion = Ollama(OLLAMA_MODEL).complete("Paul Graham is ")
        if completion:
            logging.info("Ollama test completion successful")
            print(f"Completion result: {completion}")
        else:
            logging.warning("Ollama returned empty completion")
    except Exception as e:
        logging.error(f"Error while testing Ollama: {str(e)}")


def main():
    test_ollama()


if __name__ == "__main__":
    main()
