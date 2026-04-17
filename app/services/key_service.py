import secrets
from datetime import datetime
import time

# in-memory database
api_keys_db = {}

# rate limiting config
RATE_LIMIT = 5
WINDOW = 60

# request logs
request_logs = {}

def generate_api_key():
    key = secrets.token_hex(32)

    api_keys_db[key] = {
        "created_at": datetime.utcnow(),
        "usage_count": 0
    }

    return {
        "key": key,
        "created_at": api_keys_db[key]["created_at"]
    }

def is_valid_key(key: str):
    return key in api_keys_db

def increment_usage(key: str):
    if key in api_keys_db:
        api_keys_db[key]["usage_count"] += 1

def check_rate_limit(key: str):
    now = time.time()

    if key not in request_logs:
        request_logs[key] = []

    # remove old requests
    request_logs[key] = [
        t for t in request_logs[key] if now - t < WINDOW
    ]

    if len(request_logs[key]) >= RATE_LIMIT:
        return False

    request_logs[key].append(now)
    return True