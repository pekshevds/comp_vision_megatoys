#!/bin/bash

docker stop vision-container
docker rm vision-container
docker build . -t vision
docker run -d -p 8000:8000 -v /home/pekshev/projects/comp_vision_megatoys/data:/app/data --name vision-container --restart unless-stopped vision
# docker run -it --name vision-container vision bash
