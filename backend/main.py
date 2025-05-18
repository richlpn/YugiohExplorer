import pandas as pd
import numpy as np
import os
import faiss

from fastapi import FastAPI
from sentence_transformers import SentenceTransformer

from src.schema.request_schema import QueryRequest, SearchRequest

DATA_DIR = os.getenv('DATA_DIR', './data')
app = FastAPI(
    title="Embedding API",
    description="API for generating vector embeddings using SentenceTransformer.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    debug=True,
)

# Load the model once at startup
model = SentenceTransformer('all-MiniLM-L6-v2')

df = pd.read_parquet(f'{DATA_DIR}/yugioh_cards.parquet')
index = faiss.read_index(f'{DATA_DIR}/yugioh.index')


@app.post("/embed")
def embed_query(request: QueryRequest):
    embedding = model.encode([request.query])[0]
    return {"embedding": embedding.tolist()}

@app.post("/search")
def search_query(request: SearchRequest) -> list[dict]:
    embedding = model.encode([request.query])
    filtered_embeddings = np.array(embedding)
    D, I = index.search(filtered_embeddings.astype('float32'), request.k)
    filtered_cards = df.iloc[I[0]]
    if request.types:
        filtered_cards = filtered_cards[filtered_cards['type'].isin(request.types)]
    
    if len(I) == 0:
        return {"error": "No results found."}
    
    # return the top k results as a list of dictionaries
    results = [{
            "name": filtered_cards.iloc[row]['name'],
            "image_url": filtered_cards.iloc[row]['card_images'].tolist(), # array of dict
            "desc": filtered_cards.iloc[row]['desc'], # list of dict
            "distance": int(D[0][row])} 
        for row in range(filtered_cards.shape[0])]
    return results

@app.get("/card_types")
def get_card_types() -> list:
    return list(df['type'].unique())