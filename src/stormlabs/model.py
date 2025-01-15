from typing import Literal
from pydantic_ai.models.ollama import OllamaModel
import os
from dotenv import load_dotenv

load_dotenv()

ModelSize = Literal['small', 'large', 'reasoning']

# llama3.1:8b                46e0c10c039e    4.9 GB    
# qwq:32b                    46407beda5c0    19 GB     
# qwen2.5-coder:7b           2b0496514337    4.7 GB   
# qwen2.5-coder:32b          4bd6cbf2d094    19 GB     
# nomic-embed-text:latest    0a109f422b47    274 MB    
# qwen2.5-coder:latest       2b0496514337    4.7 GB   

ollama_url = os.getenv('OLLAMA_SERVER_PATH')

MODEL_MAP = {
    'small': {
        'name': 'llama3.1:8b',
        'url': ollama_url
    },
    'large': {
        'name': 'qwen2.5-coder:32b',
        'url': ollama_url
    },
    'reasoning': {
        'name': 'qwq:32b',
        'url': ollama_url
    }
}

def stormlabs_model(size: ModelSize) -> OllamaModel:
    config = MODEL_MAP[size]
    return OllamaModel(
        model_name=config['name'],
        base_url=config['url']
    ) 