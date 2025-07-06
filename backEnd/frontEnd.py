from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/enterUrL/")
async def login(username: Annotated[str, Form()]):
    return {"username": username}