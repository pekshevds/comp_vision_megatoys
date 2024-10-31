FROM python:3
WORKDIR /app

ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && apt-get -y install cmake
RUN pip install --upgrade pip

RUN pip install cmake==3.25
RUN pip install dlib==19.24.6
RUN pip install face_recognition_models==0.3.0
RUN pip install face_recognition==1.3.0
RUN pip install imutils==0.5.4
RUN pip install opencv-python==4.10.0.84
RUN pip install python-dotenv
RUN pip install fastapi[standard]

RUN mkdir /app/upload
RUN mkdir /app/data

COPY settings.py /app/settings.py
COPY server.py /app/server.py
COPY ./services /app/services

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
