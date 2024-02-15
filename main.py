import os, uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from models.recognizeTextReq import RecognizeTextReq
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
BOT_ID = os.environ.get("BOT_ID")
BOT_ALIAS_ID = os.environ.get("BOT_ALIAS_ID")

client = LexRuntimeV2Client(bot_id=BOT_ID, bot_alias_id=BOT_ALIAS_ID)
db = {}

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "AWSLex Bot API"}


@app.post("/text/")
async def send_text(req: RecognizeTextReq):
    if req.phone_number not in db:
        db[req.phone_number] = {"context": {}}

    text = req.text
    sessionState = db[req.phone_number]["context"]
    response = client.recognize_text(text=text, sessionState=sessionState)
    newSessionState = response["sessionState"]
    db[req.phone_number]["context"] = newSessionState

    return {"response": response}


if __name__ == "__main__":
    uvicorn.run(app, port=8888, host="0.0.0.0")
