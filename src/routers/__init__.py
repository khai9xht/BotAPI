import sys
sys.path.append('./api')
sys.path.append('..')

from fastapi import APIRouter
import bot


router = APIRouter()

# TODO code include router here
# 	Eg: router.include_router(bot.router)
router.include_router(bot.router)