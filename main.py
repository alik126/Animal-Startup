from app import client, transformer, batcher

def run():
    animals = client.fetch_animals()
    print(f"Total animals fetched: {len(animals)}")
    print("Transformed animals:")
    transformed_animals = []

    for animal in animals:
        animal["friends"] = transformer.transform_friends(animal.get("friends"))
        animal["born_at"] = transformer.transform_born_at(animal.get("born_at"))
        transformed_animals.append(animal)

    print(transformed_animals)
    batches = batcher.split_batches(transformed_animals, 100)
    print(f"Posting {len(batches)} batches...")

    for idx in range(len(batches)):
        success = client.post_animals_batch(batches[idx])
        if success:
            print(f"Posted batch {idx + 1}")

if __name__ == "__main__":
    run()