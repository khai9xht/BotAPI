FROM nvcr.io/nvidia/pytorch:20.11-py3

WORKDIR /workspace

RUN mkdir botAPI

COPY ./ botAPI

WORKDIR /workspace/botAPI

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "main.py"]