FROM python:latest

COPY . /social-network

WORKDIR . /social-network

RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2525"]