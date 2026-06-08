import os
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

_client = None
db = None


async def connect_db():
    global _client, db
    url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    db_name = os.getenv("MONGODB_DB", "code_review")
    _client = motor.motor_asyncio.AsyncIOMotorClient(url)
    db = _client[db_name]
    print(f"[DB] Connected to MongoDB — database: {db_name}")


def get_db():
    return db
