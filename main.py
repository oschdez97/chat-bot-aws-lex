import os, fire
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
TESTSECRET = os.environ.get("TESTSECRET")

if __name__ == "__main__":
    print(TESTSECRET)
