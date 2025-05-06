from typing import Callable, Optional
import os
import logging
import sys
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from models.deepseek import setup_deepseek
from models.ollama import setup_ollama
from models.openrouter import setup_openrouter


def run_model(dir_path: str):
    """
    Run the RAG model with documents from the specified directory.
    
    Args:
        dir_path: Path to the directory containing documents
    """
    # Validate directory
    full_path = os.path.abspath(dir_path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Directory not found: {full_path}")
    
    if not os.path.isdir(full_path):
        raise NotADirectoryError(f"The path is not a directory: {full_path}")
    
    # Load documents with error handling
    try:
        logging.info(f"Loading documents from {full_path}...")
        documents = SimpleDirectoryReader(full_path, recursive=True).load_data()
        
        if not documents:
            raise ValueError(f"No documents found in {full_path}. Please ensure the directory contains readable files.")
        
        logging.info(f"Loaded {len(documents)} document(s)")
    except Exception as e:
        logging.error(f"Error loading documents: {str(e)}")
        raise
    
    # Create index
    try:
        logging.info("Creating vector index from documents...")
        index = VectorStoreIndex.from_documents(documents)
        logging.info("Index created successfully")
        
        # Create chat engine
        chat_engine = index.as_chat_engine()
        logging.info("Chat engine ready")
        
        # Start chat loop
        print("\n=== RAG Chat Interface ===")
        print("Type 'q' or 'bye' to exit")
        print("Type your questions below:\n")
        
        while True:
            try:
                query = input("> ").strip()
                
                # Exit conditions
                if query.lower() == "bye" or query.lower() == "q" or query.lower() == "exit":
                    print("Exiting chat. Goodbye!")
                    break
                
                # Skip empty queries
                if not query:
                    continue
                
                # Process query
                logging.info(f"Processing query: {query}")
                response = chat_engine.chat(query)
                print(f"\n{response}\n")
                
            except KeyboardInterrupt:
                print("\nReceived keyboard interrupt. Exiting...")
                break
            except Exception as e:
                logging.error(f"Error processing query: {str(e)}")
                print(f"Error: {str(e)}")
    
    except KeyboardInterrupt:
        print("\nOperation canceled by user")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error creating index: {str(e)}")
        raise


def get_setup(model: str) -> Optional[Callable]:
    """
    Get the setup function for the specified model.
    
    Args:
        model: Name of the model to use
        
    Returns:
        Setup function for the model or None if model is not recognized
    """
    model_setups = {
        "deepseek": setup_deepseek,
        "ollama": setup_ollama,
        "openrouter": setup_openrouter
    }
    
    return model_setups.get(model.lower())
