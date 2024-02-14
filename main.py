import os, fire
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
API_KEY = os.environ.get("API_KEY")

if __name__ == "__main__":
    print(os.environ)
    print(API_KEY)
