# RAGLLM: Retrieval-Augmented Generation CLI Tool

## Overview
RAGLLM is a command-line interface (CLI) tool designed to enable natural language querying of document sets using retrieval-augmented generation (RAG). It leverages large language models (LLMs) such as DeepSeek, OpenRouter, and Ollama, combined with embedding models for efficient vector-based search, to provide accurate and context-aware responses. This tool is ideal for developers, researchers, or professionals seeking to extract insights from unstructured text data.

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
- Supports multiple LLMs: DeepSeek, OpenRouter, and Ollama.
- Integrates with advanced embedding models for semantic search.
- Robust error handling and configuration validation.
- Lightweight CLI interface for ease of use.
- Modular design for extensibility and experimentation.

---

## Installation

### Prerequisites
- **Python**: Version 3.13 or higher.
- **Operating System**: Compatible with Windows, macOS, or Linux.
- **API Keys**: 
  - DeepSeek API key (required for DeepSeek model)
  - OpenRouter API key (required for OpenRouter model)
  - Ollama installed locally (required for Ollama model)

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
   Copy the `.env.example` file to `.env` in the project root and add your API keys:
   ```bash
   cp .env.example .env
   ```
   Then edit the `.env` file with your preferred text editor to add your API keys:
   ```plaintext
   # For DeepSeek
   DEEPSEEK_API_KEY=your-deepseek-api-key-here
   
   # For OpenRouter
   OPENROUTER_API_KEY=your-openrouter-api-key-here
   
   # Additional configuration options are available in the .env file
   ```
   The tool uses `dotenv` to load these variables automatically.

4. **Verify Installation**:
   Run the help command to ensure the CLI is working:
   ```bash
   python main.py --help
   ```

---

## Usage

### Command-Line Arguments
The tool accepts the following arguments:
| Argument     | Type  | Default    | Description                                               |
|--------------|-------|------------|-----------------------------------------------------------|
| `--model`    | `str` | `deepseek` | Model to use (`deepseek`, `openrouter`, or `ollama`)      |
| `directory`  | `str` | (Required) | Path to the directory with documents                      |

### Examples
1. **Query Documents with DeepSeek**:
   ```bash
   python main.py --model deepseek ./my_docs
   ```

2. **Query Documents with OpenRouter**:
   ```bash
   python main.py --model openrouter ./my_docs
   ```

3. **Query Documents with Ollama**:
   ```bash
   python main.py --model ollama ./my_docs
   ```

4. **Sample Interaction**:
   ```
   === RAG Chat Interface ===
   Type 'q' or 'bye' to exit
   Type your questions below:

   > What is the main topic of these documents?
   [Response from LLM with information from your documents]
   
   > Can you summarize the key points?
   [Summary based on document content]
   
   > bye
   Exiting chat. Goodbye!
   ```

---

## Project Structure
```
ragllm/
├── .env                   # Environment variables with API keys (not tracked in git)
├── .env.example           # Example environment variables file
├── .gitignore             # Git ignore rules
├── .python-version        # Specifies Python 3.13
├── main.py                # CLI entry point
├── models/                # Model implementations directory
│   ├── __init__.py        # Package initialization
│   ├── deepseek.py        # DeepSeek model implementation
│   ├── models.py          # Core model handling logic
│   ├── ollama.py          # Ollama model implementation
│   └── openrouter.py      # OpenRouter model implementation
├── pyproject.toml         # Project metadata and dependencies
└── wrappers/              # Test wrappers for model verification
    ├── __init__.py        # Package initialization
    ├── ollama.py          # Ollama test wrapper
    └── openrouter.py      # OpenRouter test wrapper
```

---

## Technical Details

### Supported Models
- **DeepSeek**: Uses the `deepseek/deepseek-r1:free` model via OpenRouter API.
- **OpenRouter**: Uses the `google/gemini-2.0-flash-exp:free` model or other models available on OpenRouter.
- **Ollama**: Uses the `llama3.1:8b` model with a 420-second request timeout. Requires local Ollama installation.

### Embedding Models
- **HuggingFace**: `BAAI/bge-small-en` for DeepSeek and OpenRouter queries.
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
The following environment variables can be configured in your `.env` file:

#### DeepSeek Configuration
| Variable             | Required | Description                      | Default Value                    |
|----------------------|----------|----------------------------------|----------------------------------|
| `DEEPSEEK_API_KEY`   | Yes      | API key for DeepSeek access      | -                                |
| `DEEPSEEK_BASE_URL`  | No       | Base URL for DeepSeek API        | `https://openrouter.ai/api/v1`   |
| `DEEPSEEK_MODEL`     | No       | DeepSeek model to use            | `deepseek/deepseek-r1:free`      |

#### OpenRouter Configuration
| Variable             | Required | Description                      | Default Value                    |
|----------------------|----------|----------------------------------|----------------------------------|
| `OPENROUTER_API_KEY` | Yes      | API key for OpenRouter access    | -                                |
| `OPENROUTER_MODEL`   | No       | OpenRouter model to use          | `google/gemini-2.0-flash-exp:free` |

#### Ollama Configuration
| Variable             | Required | Description                      | Default Value                    |
|----------------------|----------|----------------------------------|----------------------------------|
| `OLLAMA_MODEL`       | No       | Ollama model to use              | `llama3.1:8b`                    |

#### General Configuration
| Variable                     | Required | Description                      | Default Value                    |
|------------------------------|----------|----------------------------------|----------------------------------|
| `HUGGINGFACE_EMBEDDING_MODEL`| No       | HuggingFace embedding model      | `BAAI/bge-small-en`              |

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-improvement`).
3. Commit your changes (`git commit -m "Add my improvement"`).
4. Push to the branch (`git push origin feature/my-improvement`).
5. Open a pull request.

---

## Troubleshooting

### Common Issues and Solutions

1. **Empty Completions or API Errors**
   - **Issue**: Model returns empty completions or API errors.
   - **Solution**: Check that you've set the correct API keys in your `.env` file. Ensure the keys are valid and not expired.

2. **Configuration Failed**
   - **Issue**: "Failed to set up [model] model" error when starting the application.
   - **Solution**: The required environment variables for your chosen model are missing or incorrect. Check the "Environment Variables" section above and ensure all required variables are set.

3. **No Documents Found**
   - **Issue**: "No documents found in [directory]" error.
   - **Solution**: Ensure your directory path is correct and contains readable text files. The application supports common document formats like `.txt`, `.md`, `.pdf`, etc.

4. **Ollama Not Working**
   - **Issue**: Ollama model fails to load or respond.
   - **Solution**: Ensure Ollama is properly installed on your system and the requested model is available. Run `ollama list` to see available models and `ollama pull llama3.1:8b` to download the default model.

5. **Memory Issues**
   - **Issue**: Application crashes with memory errors when processing large document sets.
   - **Solution**: Try using smaller document sets or splitting large documents into smaller chunks.

### Testing Your Configuration

You can test each model's configuration independently using the wrapper scripts:

```bash
# Test OpenRouter configuration
python -m wrappers.openrouter

# Test Ollama configuration
python -m wrappers.ollama
```

These scripts will attempt to set up the model and perform a simple completion to verify that everything is working correctly.

## Contact
For questions or feedback, reach out to [stevenmolina2205@gmail.com] or open an issue on the GitHub repository.
