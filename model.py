from pydantic improt BaseModel


class user(BaseModel):
	user_id: str
	user_name: str


class bot(BaseModel):
	model_id: str
	model_name: str
	NLU_path: str
	action_path: str
	story_path: str
	intent_path: str
	entity_path: str
	