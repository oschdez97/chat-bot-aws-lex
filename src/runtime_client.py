import os, time, boto3
from dotenv import load_dotenv

load_dotenv(".env")
AWS_KEY = os.environ.get("AWS_KEY")
AWS_SECRET = os.environ.get("AWS_SECRET")
AWS_REGION = os.environ.get("AWS_REGION")


class LexRuntimeV2Client:
    def __init__(self, bot_id, bot_alias_id, locale_id="es_ES"):
        self.bot_id = bot_id
        self.bot_alias_id = bot_alias_id
        self.locale_id = locale_id
        self.session_id = str(time.time())
        self.client = boto3.client(
            "lexv2-runtime",
            aws_access_key_id=AWS_KEY,
            aws_secret_access_key=AWS_SECRET,
            region_name=AWS_REGION,
        )

    def recognize_text(self, text):
        """sends user prompt to the chatbot"""
        response = self.client.recognize_text(
            botId=self.bot_id,
            botAliasId=self.bot_alias_id,
            localeId=self.locale_id,
            sessionId=self.session_id,
            text=text,
        )
        return response
