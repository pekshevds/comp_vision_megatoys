FROM python:3.12-slim
# FROM python:latest

# update and install dependencies
# RUN apt-get update && apt-get install -y cmake
# RUN apt-get install build-essential cmake
# RUN apt-get install libopenblas-dev liblapack-dev
# RUN apt-get install libx11-dev libgtk-3-dev
# RUN apt-get install python python-dev python-pip
# RUN apt-get install python3 python3-dev python3-pip
RUN apt-get update &&  apt-get install -y \
	build-essential ffmpeg libsm6 libgl1 libxext6 python3-opencv
#	libopenblas-dev \
#	liblapack-dev \
#	libx11-dev \
#	libgtk-3-dev \
#	libboost-all-dev
RUN apt-get install -y cmake
WORKDIR /app
# ENV PIP_ROOT_USER_ACTION=ignore
# RUN python3 -m venv .venv && source .venv/bin/activate
# RUN pip install --upgrade pip
# RUN pip install cmake==3.25
# RUN pip3 install cmake
# RUN pip install dlib
# RUN pip3 install face_recognition_models==0.3.0
# RUN pip install face_recognition==1.3.0
# RUN pip install cmake==3.27.5
#RUN pip install distlib==0.3.7
# RUN pip install dlib==19.24.2
# RUN pip install face_recognition
# RUN pip3 install imutils==0.5.4
# RUN pip install opencv-python
# RUN pip install dlib
# RUN pip install python-dotenv
# RUN pip install fastapi[standard]


RUN mkdir /app/upload
RUN mkdir /app/data

RUN pip install dlib==19.24.2
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY settings.py /app/settings.py
COPY server.py /app/server.py
COPY ./services /app/services
COPY ./data /app/data

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
