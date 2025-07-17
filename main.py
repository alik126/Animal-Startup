from app import client, transformer, parallel


def run():
    batch = []
    page = 1

    while True:
        animals = client.fetch_animals_page(page)
        if not animals:
            break

        for animal in animals:
            animal["friends"] = transformer.transform_friends(animal.get("friends"))
            animal["born_at"] = transformer.transform_born_at(animal.get("born_at"))
            batch.append(animal)

            if len(batch) == 100:
                parallel.post_all_batches([batch])
                batch = []

        page += 1

    if batch:
        parallel.post_all_batches([batch])


if __name__ == "__main__":
    run()
