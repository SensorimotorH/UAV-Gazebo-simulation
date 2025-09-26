from fastapi import FastAPI
from pydantic import BaseModel


from backend.app import product_apirouter
from fastapi.middleware.cors import CORSMiddleware
from agent_config import conf
import os

import logging
logging.basicConfig(
    level=logging.INFO, format="%(name)s-%(levelname)s-%(message)s"
)
logger = logging.getLogger(__name__)

class InputItem(BaseModel):
    input_str: str

origins = [
    "http://127.0.0.1:8081",
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    product_apirouter(conf),
    prefix=conf.get("APIUrl", "prefix"),
    tags=["api"],
    responses={404: {"description": "Not found"}},
)
@app.get("/")
async def read_root():
    return {"Hello": "World"}
