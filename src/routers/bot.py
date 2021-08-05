from fastapi import APIRouter, Depends, status
import models 
import config 
from utils import zipfolder
from fastapi.responses import FileResponse


router = APIRouter()

@router.post("/bot/start")
async def start(user: models.User, bot: models.Bot)
	pass

@router.get("/bot/response")
async def response(user: models.User, message: str):
	pass

@router.post("/bot/parse")
async def parse(user: models.User, message: str):
	pass

@router.post("/bot/import")
async def import(bot: models.Bot):
	pass

@router.get("/bot/export")
async def export(user: models.User, bot: models.Bot):
	# check bot exists and in user through user id

	# zip folder bot and send to client
	bot_path = os.path.join(config.Bot_path, bot.name)
	botname_zip = models.bot.name + ".zip" 
	zipfolder(bot_path, botname_zip)

	return FileResponse(path=botname_zip, filename=botname_zip)