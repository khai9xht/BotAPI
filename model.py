from pydantic import BaseModel


class User(BaseModel):
	user_id: str
	user_name: str


class Bot(BaseModel):
	bot_id: str
	bot_name: str
	models_path: str
	action_path: str
	data_path: str
	tests_path: str
	config_path: str