FROM continuumio/anaconda3
WORKDIR /app

RUN conda install -n base libarchive -c main --force-reinstall
RUN conda install -n base conda-libmamba-solver --solver=classic
RUN conda install -c conda-forge dlib
RUN pip install opencv-python
RUN pip install face_recognition
RUN pip install imutils
RUN pip install python-dotenv
RUN pip install fastapi[standard]

RUN mkdir /app/upload
RUN mkdir /app/data

COPY settings.py /app/settings.py
COPY server.py /app/server.py
COPY ./services /app/services

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
