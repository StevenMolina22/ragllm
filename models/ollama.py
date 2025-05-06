from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")


def setup_ollama():
    Settings.llm = Ollama(model=OLLAMA_MODEL, request_timeout=420)
    Settings.embed_model = OllamaEmbedding(model_name=OLLAMA_MODEL)
