from fastapi import FastAPI
from pydantic import BaseModel
from .gemni_services import generate_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "chrome-extension://igahbolgfebmfkoknmjdbgbleiaieofe",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class request_type(BaseModel):
    text:str
    tone:str

@app.post('/grammar_fix')
async def grammar_fix(input:request_type):
    result = generate_text(text=input.text, tone= input.tone)
    return {"result": result}