import concurrent.futures
from app import client
from typing import List


def post_all_batches(batches: List, max_workers: int = 5) -> None:
    """
    Post all batches in parallel using a thread pool.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []

        for batch in batches:
            futures.append(executor.submit(client.post_animals_batch, batch))

        for i, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            try:
                future.result()
                print(f"Posted batch")
            except Exception as e:
                print(f"Failed to post batch {i}: {e}")
