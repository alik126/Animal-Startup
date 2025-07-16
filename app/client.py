import requests
from typing import List
from app.config import BASE_URL


def fetch_animals() -> List[dict]:
    """
    Fetch all animals using pagination.
    """
    all_animals = []
    page = 1

    while True:
        url = f"{BASE_URL}/animals/v1/animals?page={page}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        items = data.get("items", [])
        if not items:
            break

        all_animals.extend(items)

        if page >= data.get("total_pages", 0):
            break

        page += 1

    return all_animals
