FROM continuumio/miniconda3
WORKDIR /app

RUN conda install -c conda-forge dlib
RUN pip install opencv-python
RUN pip install face_recognition
RUN pip install imutils
RUN pip install python-dotenv
RUN pip install django

COPY lib.py .
COPY face_enc .
COPY manage.py .
COPY ./server ./server
COPY ./index ./index
COPY ./upload ./upload

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
