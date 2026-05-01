from pydantic import BaseModel

class Settings(BaseModel):
    # llm_model: str = "gpt-3.5-turbo"
    # embedding_model: str = "text-embedding-3-small"
    # max_tokens: int = 2048
    # temperature: float = 0.7
    # top_p: float = 1.0
    # frequency_penalty: float = 0.0
    # presence_penalty: float = 0.0
    app_name: str = "Enterprise Support Agent"
    app_version: str = "0.1.0"
    
settings = Settings()