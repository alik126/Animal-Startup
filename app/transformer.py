from typing import Optional, List
from datetime import datetime, timezone

def transform_friends(friends: Optional[str]) -> List[str]:
    if not friends:
        return []

    result = []
    for name in friends.split(","):
        name = name.strip()
        if name:
            result.append(name)

    return result

def transform_born_at(born_at: Optional[int]) -> Optional[str]:
    if not born_at:
        return None

    seconds = born_at / 1000
    dt = datetime.fromtimestamp(seconds, timezone.utc)
    return dt.isoformat().replace("+00:00", "Z")