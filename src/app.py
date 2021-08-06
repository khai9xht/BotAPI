from fastapi import FastAPI, Request 
import requests
import subprocess
from models import User, Bot
import routers

app = FastAPI() 


@app.get('/')
def read_root():
	return {"message": "Welcome to Bot Testing API"}

@app.get('/botreply')
def BotReply(user: str, user_ulter: str):
	response = requests.post(
		"http://192.168.50.17:5005/webhooks/rest/webhook",
		json = {
			"sender": user,
			"message": user_ulter
		}
	)
	return response.json()

@app.get('/parse')
async def parse(message: str, message_id: str):
	response = requests.post(
		"http://192.168.50.17:5005/model/parse",
		json = {
			"text": message,
			"message_id": nessage_id
		}    
	)
	return response.json()

@app.post('/start')
async def start(user_id):
	shellscript = subprocess.Popen(["run_botapi.sh"], stdin=subprocess.PIPE)
	return {"message": "install successfully!"}

app.include_router(routers.router)