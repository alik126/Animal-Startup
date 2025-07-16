def transform_friends(friends):
    if not friends:
        return []

    result = []
    for name in friends.split(","):
        name = name.strip()
        if name:
            result.append(name)

    return result