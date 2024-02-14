import os, fire
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
BOT_ID = os.environ.get("BOT_ID")
BOT_ALIAS_ID = os.environ.get("BOT_ALIAS_ID")

def test_lex_client():
    client = LexRuntimeV2Client(bot_id=BOT_ID, bot_alias_id=BOT_ALIAS_ID)
    assert client is not None
    assert isinstance(client, LexRuntimeV2Client)