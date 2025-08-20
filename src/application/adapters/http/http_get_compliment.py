from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from application.application.get_complment_app import get_compliment
from modules.text_processor.core.ports.i_mode import ModeType

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

class ModeRequest(BaseModel):
    mode: str

class ImageCaptionRequest(BaseModel):
    url: str

@app.get("/get-mode")
def get_mode():
    return {"response": get_compliment.get_mode()}

@app.post("/set-mode")
def set_mode(request: ModeRequest):
    get_compliment.set_mode(ModeType(request.mode.upper()))
    return {"response": request.mode}

@app.post("/describe-image")
def describe_image(request: ImageCaptionRequest):
    caption = get_compliment.describe_image(request.url)
    return {"response": caption}