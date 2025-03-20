from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
import sys

def setup_ollama():
    Settings.llm = Ollama(
        model="llama3.1:8b",
        request_timeout=420
    )
    Settings.embed_model = OllamaEmbedding(model_name="llama3.1:8b")

def main():
    directory = sys.argv[1]

    setup_ollama()
    documents = SimpleDirectoryReader(f"../{directory}").load_data()
    index = VectorStoreIndex.from_documents(documents)

    query = input("> ")
    response = index.as_query_engine().query(query)
    print(response)

if __name__ == "__main__":
    main()
