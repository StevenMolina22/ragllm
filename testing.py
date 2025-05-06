from dotenv.main import load_dotenv
from llama_index.llms.openrouter import OpenRouter
from llama_index.core.llms import ChatMessage
import os

load_dotenv()

llm = OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    max_tokens=256,
    context_window=32768,
    model=os.getenv("OPENROUTER_MODEL", ""),
)


def run_model(dir: str):
    message = ChatMessage(role="user", content="Tell me a joke")
    resp = llm.chat([message])
    print(resp)


if __name__ == "__main__":
    run_model(".")
