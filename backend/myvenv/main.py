# from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def redirect_react():
    return RedirectResponse(url="http://localhost:3000/")
