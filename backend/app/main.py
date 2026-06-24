from fastapi import FastAPI, HTTPException
from .gemni_services import generate_text, GeminiBusyError
from fastapi.middleware.cors import CORSMiddleware
from .models import request_type
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


@app.post('/grammar_fix')
async def grammar_fix(input:request_type):
    try:
        result = generate_text(text=input.text, tone=input.tone)
        return {"result": result}

    except GeminiBusyError:
        raise HTTPException(
            status_code=503,
            detail="Grammar service is temporarily busy. Please try again in a few seconds."
        )

    except Exception as e:
        print("Unexpected error:", e)
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while generating text."
        )
