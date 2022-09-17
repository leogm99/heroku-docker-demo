import logging

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import databases
import os

# loads env variables from .env file
# .env files should not be commited to github (add to .gitignore)
ENV = os.environ
load_dotenv('../.env')

# db connection
database = databases.Database(ENV['DATABASE_URL'])

app = FastAPI()


@app.on_event('startup')
async def startup():
	await database.connect()


@app.on_event('shutdown')
async def shutdown():
	await database.disconnect()


@app.get("/")
async def hello_world():
	return ENV.get('HELLO')


@app.get("/greeting/{name}")
async def greetings(name: str):
	return f"Hola {name}! Te quiero mucho <3"


@app.get("/user/{uid}")
async def get_user(uid: int):
	return uid


if __name__ == '__main__':
	uvicorn.run("app.main:app", host="0.0.0.0", port=int(ENV.get('PORT')), log_level="info", reload=True)
