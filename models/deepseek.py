from llama_index.core import Settings
from llama_index.llms.deepseek import DeepSeek
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv
import os
import logging

load_dotenv()

HUGGINGFACE_EMBEDDING_MODEL = os.getenv(
    "HUGGINGFACE_EMBEDDING_MODEL", "BAAI/bge-small-en"
)


def setup_deepseek() -> bool:
    """
    Setup DeepSeek model configuration with environment variable validation.
    
    Returns:
        bool: True if setup was successful, False otherwise
    """
    # Validate required environment variables
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    deepseek_base_url = os.getenv("DEEPSEEK_BASE_URL", "https://openrouter.ai/api/v1")
    deepseek_model = os.getenv("DEEPSEEK_MODEL", "deepseek/deepseek-r1:free")
    
    # Check if API key is present
    if not deepseek_api_key:
        logging.error("Missing required environment variable: DEEPSEEK_API_KEY")
        return False
    
    # Configure DeepSeek
    try:
        Settings.llm = DeepSeek(
            api_key=deepseek_api_key,
            api_base=deepseek_base_url,
            model=deepseek_model,
        )
        logging.info(f"DeepSeek LLM configured successfully with model: {deepseek_model}")
        
        # Configure embedding model
        Settings.embed_model = HuggingFaceEmbedding(model_name=HUGGINGFACE_EMBEDDING_MODEL)
        logging.info(f"HuggingFace embedding model configured successfully: {HUGGINGFACE_EMBEDDING_MODEL}")
        
        return True
    except Exception as e:
        logging.error(f"Failed to setup DeepSeek configuration: {str(e)}")
        return False
