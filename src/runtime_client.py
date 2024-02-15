import os, time, boto3
from dotenv import load_dotenv

load_dotenv(".env")
IAM_KEY = os.environ.get("IAM_KEY")
IAM_SECRET = os.environ.get("IAM_SECRET")
AWS_REGION = os.environ.get("REGION")


class LexRuntimeV2Client:
    def __init__(self, bot_id, bot_alias_id, locale_id="es_ES"):
        self.bot_id = bot_id
        self.bot_alias_id = bot_alias_id
        self.locale_id = locale_id
        self.session_id = str(time.time())
        self.client = boto3.client(
            "lexv2-runtime",
            aws_access_key_id=IAM_KEY,
            aws_secret_access_key=IAM_SECRET,
            region_name=AWS_REGION,
        )

    def recognize_text(self, text, sessionState):
        """Sends user prompt to the chatbot"""
        response = self.client.recognize_text(
            botId=self.bot_id,
            botAliasId=self.bot_alias_id,
            localeId=self.locale_id,
            sessionId=self.session_id,
            text=text,
            sessionState=sessionState,
        )
        if response is not None:
            intent_dict_clean = {
                k: ({} if v is None else v)
                for k, v in response["sessionState"]["intent"]["slots"].items()
            }
            response["sessionState"]["intent"]["slots"] = intent_dict_clean

        return response
