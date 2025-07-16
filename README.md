# Animal-Startup

This is a Python ETL-style tool that:

- Fetches animal data from a local API
- Transforms the `friends` and `born_at` fields
- Sends the animals in batches of 100
- Handles random server delays and errors

---

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the system

Make sure the API server is already running on:

```bash
http://localhost:3123
```

Then run:

```bash
python main.py
```

You’ll see logs for fetched animals and posted batches.

### 4. Run tests

```bash
PYTHONPATH=. pytest
```

### 5. Lint and Format (Optional, as it is already done)

```bash
flake8 app/ tests/
black app/ tests/ --check
```

#### Notes

Transforms:

```bash
friends: comma string → list of names
born_at: ms timestamp → ISO 8601 UTC
```

Posts batches in parallel with retry logic

Keeps code clean, readable, and testable
