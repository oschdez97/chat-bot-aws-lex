import os
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
BOT_ID = os.environ.get("BOT_ID")
BOT_ALIAS_ID = os.environ.get("BOT_ALIAS_ID")

if __name__ == "__main__":
    client = LexRuntimeV2Client(bot_id=BOT_ID, bot_alias_id=BOT_ALIAS_ID)
    resp = client.recognize_text("Hola!")
    print(resp)
