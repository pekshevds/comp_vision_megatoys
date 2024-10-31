#!/bin/bash

docker stop vision-container
docker rm vision-container
docker build . -t vision
#docker run -d -p 8000:8000 -v /home/pekshev/projects/comp_vision_megatoys/data:/app/data --name anaconda1 anaconda
docker run -it -p 8000:8000 -v /home/pekshev/projects/comp_vision_megatoys/data:/app/data --name vision-container vision bash

