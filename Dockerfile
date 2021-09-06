FROM ubuntu:18.04

RUN  apt update && apt install -y \
    software-properties-common \
    python python-pip

# last supported opencv version for python2
RUN pip2 install opencv-python-headless==4.2.0.32 

WORKDIR /retinex
COPY ./run-headless.py ./config.json ./retinex.py /retinex/

VOLUME ["/data"]
VOLUME ["/results"]

CMD ["python", "run-headless.py", "/data", "/results"]