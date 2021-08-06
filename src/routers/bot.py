from fastapi import APIRouter, Depends, status
from fastapi import File, UploadFile
import models 
import config 
from utils import zipfolder, unzip_folder
from fastapi.responses import FileResponse
import os


router = APIRouter(
	prefix='/bot',
	tags=['bot'],
)

@router.post("/start")
async def start(user: models.User, bot: models.Bot):
	pass

@router.get("/response")
async def response(user: models.User, message: str):
	pass

@router.post("/parse")
async def parse(user: models.User, message: str):
	pass

@router.post(
	"/import", 
	status_code=status.HTTP_201_CREATED,
)
async def bot_import(bot: UploadFile = File(...)):
	unzip_folder(bot.file, config.Bot_path)

@router.post(
	"/export", 
	status_code=status.HTTP_201_CREATED,
	response_model=FileResponse
)
async def bot_export(user: models.User, bot: models.Bot):
	# check bot exists and in user through user id

	# zip folder bot and send to client
	bot_path = os.path.join(config.Bot_path, bot.name)
	botname_zip = bot.name + ".zip" 
	zipfolder(bot_path, botname_zip)

	return FileResponse(path=botname_zip, filename=botname_zip)