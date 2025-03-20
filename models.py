from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.deepseek import DeepSeek
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

from dotenv import load_dotenv
import os

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://openrouter.ai/api/v1")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek/deepseek-r1:free")

HUGGINGFACE_EMBEDDING_MODEL = os.getenv("HUGGINGFACE_EMBEDDING_MODEL", "BAAI/bge-small-en")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

def setup_deepseek():
    Settings.llm = DeepSeek(
        api_key=DEEPSEEK_API_KEY,
        api_base=DEEPSEEK_BASE_URL,
        model=DEEPSEEK_MODEL,
    )
    Settings.embed_model = HuggingFaceEmbedding(model_name=HUGGINGFACE_EMBEDDING_MODEL)

def setup_ollama():
    Settings.llm = Ollama(
        model=OLLAMA_MODEL,
        request_timeout=420
    )
    Settings.embed_model = OllamaEmbedding(model_name=OLLAMA_MODEL)

def run_ollama(dir: str):
    setup_ollama()
    documents = SimpleDirectoryReader(f"./{dir}").load_data()
    index = VectorStoreIndex.from_documents(documents)

    while True:
        query = input("> ")
        if query.lower() == "bye" or query == "q".lower():
            break
        response = index.as_query_engine().query(query)
        print(response)

def run_deepseek(dir: str):
    setup_deepseek()
    documents = SimpleDirectoryReader(f"./{dir}").load_data()
    index = VectorStoreIndex.from_documents(documents)

    while True:
        query = input("> ")
        if query.lower() == "bye" or query == "q".lower():
            break
        response = index.as_query_engine().query(query)
        print(response)
