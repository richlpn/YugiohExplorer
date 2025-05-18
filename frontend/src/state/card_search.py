from src.schema.card import Card
import httpx
from logging import getLogger
API_URL = "http://search_embeddings:8000"

async def search(query, k:int = 5, types_filters: list[str] | None = None) -> list[Card]:
    logger = getLogger(__name__)
    async with httpx.AsyncClient() as client:
        data = {
            "query": query,
            "k": k,
            "types": types_filters or []
        }
        response = await client.post(f'{API_URL}/search', json=data)
        if response.status_code != 200:
            response.raise_for_status()
        results = response.json()
        logger.debug(results)
    return [Card.model_validate(card) for card in results] if results else []
            

async def get_card_types() -> list[str]:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/card_types")
        results = response.json()
    return results if results else []