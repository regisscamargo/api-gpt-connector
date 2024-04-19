FROM python:3.8-slim

RUN apt-get update && apt-get install -y apt-transport-https

RUN apt-get update && apt-get install -qq -y \
    build-essential python3.8-dev libssl-dev libffi-dev --no-install-recommends

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN python -m pip install --upgrade pip setuptools wheel

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

EXPOSE 5500
