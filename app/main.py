import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
	return "Hello World"


@app.get("/greeting/{name}")
async def greetings(name: str):
	return f"Hola {name}! Te quiero mucho <3"

