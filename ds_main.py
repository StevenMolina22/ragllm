from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.deepseek import DeepSeek
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv
import os
import sys

load_dotenv()
API_KEY=os.getenv("DEEPSEEK_API_KEY")
BASE_URL="https://openrouter.ai/api/v1"
MODEL="deepseek/deepseek-r1:free"

def setup_ollama():
    Settings.llm = DeepSeek(
        model=MODEL,
        api_base=BASE_URL,
        api_key=API_KEY,
    )
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

def main():
    if len(sys.argv) <= 1:
        print("Specify a directory.")
        return
    directory = sys.argv[1]

    setup_ollama()
    documents = SimpleDirectoryReader(f"../{directory}").load_data()
    index = VectorStoreIndex.from_documents(documents)

    while True:
        query = input("> ")
        if query.lower() == "bye" or query == "q".lower():
            break
        response = index.as_query_engine().query(query)
        print(response)

if __name__ == "__main__":
    main()
