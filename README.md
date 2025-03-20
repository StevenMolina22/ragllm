# RAGLLM: Retrieval-Augmented Generation CLI Tool

## Overview
RAGLLM is a command-line interface (CLI) tool designed to enable natural language querying of document sets using retrieval-augmented generation (RAG). It leverages large language models (LLMs) such as DeepSeek and Ollama, combined with embedding models for efficient vector-based search, to provide accurate and context-aware responses. This tool is ideal for developers, researchers, or professionals seeking to extract insights from unstructured text data.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
   - [Command-Line Arguments](#command-line-arguments)
   - [Examples](#examples)
4. [Project Structure](#project-structure)
5. [Technical Details](#technical-details)
   - [Supported Models](#supported-models)
   - [Embedding Models](#embedding-models)
   - [Dependencies](#dependencies)
6. [Configuration](#configuration)
   - [Environment Variables](#environment-variables)
7. [Contributing](#contributing)
8. [Contact](#contact)

---

## Features
- Query documents using natural language with RAG techniques.
- Supports multiple LLMs: DeepSeek and Ollama.
- Integrates with advanced embedding models for semantic search.
- Lightweight CLI interface for ease of use.
- Modular design for extensibility and experimentation.

---

## Installation

### Prerequisites
- **Python**: Version 3.13 or higher.
- **Operating System**: Compatible with Windows, macOS, or Linux.
- **API Key**: A DeepSeek API key from OpenRouter (required for DeepSeek model).

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/StevenMolina22/ragllm.git
   cd ragllm
   ```

2. **Install Dependencies**:
   Ensure you have `uv` or `pip` installed, then run:
   ```bash
   uv sync  # Preferred, if using uv
   # OR
   pip install .
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add your DeepSeek API key:
   ```plaintext
   DEEPSEEK_API_KEY=your-api-key-here
   ```
   The tool uses `dotenv` to load this automatically.

4. **Verify Installation**:
   Run the help command to ensure the CLI is working:
   ```bash
   python main.py --help
   ```

---

## Usage

### Command-Line Arguments
The tool accepts the following arguments:
| Argument     | Type  | Default    | Description                          |
|--------------|-------|------------|--------------------------------------|
| `--model`    | `str` | `deepseek` | Model to use (`deepseek` or `ollama`)|
| `directory`  | `str` | (Required) | Path to the directory with documents|

### Examples
1. **Query Documents with DeepSeek**:
   ```bash
   python main.py --model deepseek ./my_docs
   ```
   After launching, type a query (e.g., "What is the main topic?") and press Enter. Type `bye` or `q` to exit.

2. **Query Documents with Ollama**:
   ```bash
   python main.py --model ollama ./my_docs
   ```

3. **Sample Interaction**:
   ```
   > What is the summary of the first document?
   [Response from LLM]
   > bye
   ```

---

## Project Structure
```
ragllm/
├── example_snippets/    # Example scripts (e.g., deepseek.py)
├── .gitignore           # Git ignore rules
├── .python-version      # Specifies Python 3.13
├── main.py              # CLI entry point
├── models.py            # Core logic for model setup and querying
├── pyproject.toml       # Project metadata and dependencies
└── .env                 # Environment variables (not tracked)
```

---

## Technical Details

### Supported Models
- **DeepSeek**: Uses the `deepseek/deepseek-r1:free` model via OpenRouter API.
- **Ollama**: Uses the `llama3.1:8b` model with a 420-second request timeout.

### Embedding Models
- **HuggingFace**: `BAAI/bge-small-en` for DeepSeek queries.
- **Ollama**: `llama3.1:8b` embeddings for Ollama queries.

### Dependencies
Key libraries include:
- `llama-index` (v0.12.24+): Core RAG functionality.
- `openai` (v1.66.3+): API client for DeepSeek.
- `llama-index-embeddings-huggingface` (v0.5.2+): Embedding support.
See `pyproject.toml` for the full list.

---

## Configuration

### Environment Variables
| Variable          | Description                   | Example Value                          |
|-------------------|-------------------------------|----------------------------------------|
| `DEEPSEEK_API_KEY`| API key for DeepSeek access   | `sk-or-v1-...`                        |

The `BASE_URL` and `MODEL` are hardcoded in `models.py` but can be modified for flexibility.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-improvement`).
3. Commit your changes (`git commit -m "Add my improvement"`).
4. Push to the branch (`git push origin feature/my-improvement`).
5. Open a pull request.

---

## Contact
For questions or feedback, reach out to [stevenmolina2205@gmail.com] or open an issue on the GitHub repository.
