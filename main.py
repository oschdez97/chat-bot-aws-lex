import os, fire
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
API_KEY = os.environ.get("SECRETO")

if __name__ == "__main__":
    print(os.environ)
    print(API_KEY)

    with open(".env", "r") as f:
        secret = f.readline().split("=")[1].strip()
        print(secret)
