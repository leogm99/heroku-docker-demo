import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
	return "Hello World"


@app.get("/greeting/{name}")
async def hello_world(name: str):
	return f"Hola {name}! Te quiero mucho <3"


if __name__ == '__main__':
	import os
	# heroku assigns port as an env variable
	port = os.environ["PORT"]
	uvicorn.run("app.main:app", host="0.0.0.0", port=port)
