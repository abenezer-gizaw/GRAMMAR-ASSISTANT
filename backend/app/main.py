from fastapi import FastAPI
from pydantic import BaseModel
from .gemni_services import generate_text

app = FastAPI()

class request_type(BaseModel):
    text:str
    tone:str

@app.post('/grammar_fix')
async def grammar_fix(input:request_type):
    result = generate_text(text=input.text, tone= input.tone)
    return {"result": result}