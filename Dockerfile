FROM python:3.12-slim
RUN apt-get update &&  apt-get install -y build-essential ffmpeg libsm6 libgl1 libxext6 python3-opencv
RUN apt-get install -y cmake

WORKDIR /app

RUN mkdir /app/upload
RUN mkdir /app/data

# RUN pip install dlib==19.24.2
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY settings.py /app/settings.py
COPY server.py /app/server.py
COPY ./utils /app/utils
COPY ./data /app/data
COPY ./templates /app/templates

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
