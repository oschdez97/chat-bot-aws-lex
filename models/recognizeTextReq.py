from pydantic import BaseModel

class RecognizeTextReq(BaseModel):
    phone_number: str
    text: str