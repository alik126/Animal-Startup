from app import client, transformer

def run():
    animals = client.fetch_animals()
    print(f"Total animals fetched: {len(animals)}")
    print("Transformed animals:")
    transformed_animals = []

    for animal in animals:
        animal["friends"] = transformer.transform_friends(animal.get("friends"))
        animal["born_at"] = transformer.transform_born_at(animal.get("born_at"))
        transformed_animals.append(animal)

    for animal in transformed_animals:
        print(animal)

if __name__ == "__main__":
    run()