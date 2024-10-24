# comp_vision_megatoys

create Images folder in root folder
create the named folders in Images folder
fill the named folders with images

for example
Images
    |name1
        |pic1.jpg
        |pic1.jpg
        ...
        |picN.jpg
    |name2
        |pic1.jpg
        |pic1.jpg
        ...
        |picN.jpg
    ...
    |nameN
        |pic1.jpg
        |pic1.jpg
        ...
        |picN.jpg

download and install
https://www.anaconda.com/download

install packages
****************
conda install -c conda-forge dlib
pip install opencv-python
pip install face_recognition
pip install imutils
pip install fastapi[standard]

http://127.0.0.1:8081/get-mask
multipart/form-data
docker run -i -t -p 8081:8081 continuumio/miniconda3
