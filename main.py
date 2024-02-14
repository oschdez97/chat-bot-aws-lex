import os, fire, boto3
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
IAM_KEY = os.environ.get("IAM_KEY")
IAM_SECRET = os.environ.get("IAM_SECRET")
AWS_REGION = os.environ.get("REGION")

if __name__ == "__main__":
    print([IAM_KEY, IAM_SECRET, AWS_REGION])

    client = boto3.client(
        "lexv2-runtime",
        aws_access_key_id=IAM_KEY,
        aws_secret_access_key=IAM_SECRET,
        region_name=AWS_REGION
    )
    print(client)
    
