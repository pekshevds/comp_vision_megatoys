FROM continuumio/miniconda3
WORKDIR /app

RUN conda install -c conda-forge dlib
RUN pip install opencv-python
RUN pip install face_recognition
RUN pip install imutils
RUN pip install python-dotenv
RUN pip install fastapi[standard]

RUN mkdir upload

COPY settings.py .
COPY server.py .
COPY ./services ./services
COPY ./data ./data

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
