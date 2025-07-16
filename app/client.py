import requests, time
from time import sleep
from typing import List, Dict
from app.config import BASE_URL, FETCH_ENDPOINT, POST_ENDPOINT, MAX_RETRIES, TIMEOUT


def fetch_animals() -> List[dict]:
    """
    Fetch all animals using pagination with retry (upto 5 times) on server errors.
    """
    all_animals = []
    page = 1

    while True:
        url = f"{BASE_URL}{FETCH_ENDPOINT}?page={page}"

        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(url, timeout=TIMEOUT)
                if response.status_code in {500, 502, 503, 504}:
                    raise requests.RequestException(
                        f"Server error {response.status_code}"
                    )
                break
            except requests.RequestException as e:
                print(
                    f"[Retry {attempt + 1}/{MAX_RETRIES}] Failed to fetch page {page}: {e}"
                )
                sleep(2)

        else:
            raise Exception(f"Failed to fetch page {page} after {MAX_RETRIES} retries.")

        data = response.json()

        items = data.get("items", [])
        if not items:
            break

        all_animals.extend(items)

        if page >= data.get("total_pages", 0):
            break

        page += 1

    return all_animals


def post_animals_batch(batch: List[Dict]) -> bool:
    url = f"{BASE_URL}{POST_ENDPOINT}"

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(url, json=batch, timeout=TIMEOUT)
            print(response.status_code, response.text)

            if response.status_code in [500, 502, 503, 504]:
                raise Exception(f"Server error {response.status_code}")

            return True

        except Exception as e:
            print(f"[Retry {attempt + 1}/{MAX_RETRIES}] Failed to post batch: {e}")
            time.sleep(2)

    raise Exception(f"Failed to post batch after {MAX_RETRIES} attempts.")
