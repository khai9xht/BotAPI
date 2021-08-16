from pydantic import BaseModel

class Bot(BaseModel):
	id: str
	name: str
	# models_path: str
	# action_path: str
	# data_path: str
	# tests_path: str
	# config_path: str