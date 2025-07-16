import requests
from time import sleep
from typing import List
from app.config import BASE_URL


def fetch_animals() -> List[dict]:
    """
    Fetch all animals using pagination with retry (upto 5 times) on server errors.
    """
    all_animals = []
    page = 1

    while True:
        url = f"{BASE_URL}/animals/v1/animals?page={page}"

        for attempt in range(5):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code in {500, 502, 503, 504}:
                    raise requests.RequestException(f"Server error {response.status_code}")
                break
            except requests.RequestException as e:
                print(f"[Retry {attempt + 1}/5] Failed to fetch page {page}: {e}")
                sleep(2)

        else:
            raise Exception(f"Failed to fetch page {page} after 5 retries.")

        data = response.json()

        items = data.get("items", [])
        if not items:
            break

        all_animals.extend(items)

        if page >= data.get("total_pages", 0):
            break

        page += 1

    return all_animals
