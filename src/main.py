import uvicorn
from settings import settings

if __name__ == "__main__":
	uvicorn.run(
		"app:app",
		host=settings.SERVER_HOST,
		port=settings.SERVER_PORT,
		reload=True,
	)