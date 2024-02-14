import os, fire
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

env_file = os.getenv('GITHUB_ENV')

if __name__ == "__main__":
    print(env_file)
