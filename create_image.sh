#!/bin/bash

docker stop anaconda1
docker rm anaconda1
docker build . -t anaconda
#docker run -d -p 8000:8000 -v /home/pekshev/projects/comp_vision_megatoys/data:/app/data --name anaconda1 anaconda
docker run -it -p 8000:8000 -v /home/pekshev/projects/comp_vision_megatoys/data:/app/data --name anaconda1 anaconda bash

