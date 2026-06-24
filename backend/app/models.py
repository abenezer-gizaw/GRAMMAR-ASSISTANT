from pydantic import BaseModel

class request_type(BaseModel):
    text:str
    tone:str