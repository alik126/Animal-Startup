from typing import List


def split_batches(data: List, batch_size: int) -> List[List]:
    result = []
    for i in range(0, len(data), batch_size):
        result.append(data[i : i + batch_size])
    return result
