from motor.motor_asyncio import AsyncIOMotorClient
from core.config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client.snapskill # Database name
