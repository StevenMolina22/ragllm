from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.deepseek import DeepSeek
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

from dotenv import load_dotenv
import os

load_dotenv()
DEEPSEEK_API_KEY=os.getenv("DEEPSEEK_API_KEY")
BASE_URL="https://openrouter.ai/api/v1"
MODEL="deepseek/deepseek-r1:free"

def setup_deepseek():
    Settings.llm = DeepSeek(
        model=MODEL,
        api_base=BASE_URL,
        api_key=DEEPSEEK_API_KEY,
    )
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

def setup_ollama():
    Settings.llm = Ollama(
        model="llama3.1:8b",
        request_timeout=420
    )
    Settings.embed_model = OllamaEmbedding(model_name="llama3.1:8b")

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
