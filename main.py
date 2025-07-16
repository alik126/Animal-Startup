from app import client

def run():
    animals = client.fetch_animals()
    print(f"Total animals fetched: {len(animals)}")

if __name__ == "__main__":
    run()