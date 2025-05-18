from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str

class SearchRequest(QueryRequest):
    k: int = 5
    types: list[str] = Field(default_factory=list)