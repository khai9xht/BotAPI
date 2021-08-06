FROM ubuntu:latest

ENV DEBIAN_FONTEND=noninteractive

RUN apt-get update && apt-get install git vim -y

RUN apt-get install -y python3-pip python3-dev -y \
	&& cd /usr/local/bin \
	&& ln -s /user/bin/python3 python 

WORKDIR /home

RUN mkdir botAPI

COPY ./ botAPI

WORKDIR /home/botAPI

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /home/botAPI/src

# CMD ["/usr/bin/python3", "main.py"]