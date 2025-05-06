from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openrouter import OpenRouter
from dotenv import load_dotenv
import os
import logging

load_dotenv()

HUGGINGFACE_EMBEDDING_MODEL = os.getenv(
    "HUGGINGFACE_EMBEDDING_MODEL", "BAAI/bge-small-en"
)


def setup_openrouter() -> bool:
    """
    Setup OpenRouter model configuration with environment variable validation.
    
    Returns:
        bool: True if setup was successful, False otherwise
    """
    # Validate required environment variables
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    openrouter_model = os.getenv("OPENROUTER_MODEL", "google/gemini-2.0-flash-exp:free")
    
    # Check if API key is present
    if not openrouter_api_key:
        logging.error("Missing required environment variable: OPENROUTER_API_KEY")
        return False
    
    # Configure OpenRouter
    try:
        Settings.llm = OpenRouter(
            api_key=openrouter_api_key,
            model=openrouter_model,
        )
        logging.info(f"OpenRouter LLM configured successfully with model: {openrouter_model}")
        
        # Configure embedding model
        Settings.embed_model = HuggingFaceEmbedding(model_name=HUGGINGFACE_EMBEDDING_MODEL)
        logging.info(f"HuggingFace embedding model configured successfully: {HUGGINGFACE_EMBEDDING_MODEL}")
        
        return True
    except Exception as e:
        logging.error(f"Failed to setup OpenRouter configuration: {str(e)}")
        return False
