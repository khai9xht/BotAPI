docker rm -f BotApi
docker image rm -f botapi
docker build . --file Dockerfile --tag botapi
docker run --name BotApi -it -d \
	-p 6789:6789 -p 9876:9876 \
	-v /home/data_nfs/hoangnv/BotTestingAPI/src:/home/botAPI/src \
	botapi