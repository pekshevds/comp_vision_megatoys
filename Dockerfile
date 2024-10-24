FROM continuumio/miniconda3
WORKDIR /app

RUN conda install -c conda-forge dlib
RUN pip install opencv-python
RUN pip install face_recognition
RUN pip install imutils
RUN pip install fastapi[standard]

COPY lib.py .
COPY server.py .
COPY face_enc .
COPY ./Images ./Images
COPY ./upload ./upload

EXPOSE 8081

CMD ["uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8081"]
