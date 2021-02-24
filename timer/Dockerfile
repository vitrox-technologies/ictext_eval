FROM nvidia/cuda:10.2-runtime-ubuntu18.04
RUN apt update && apt install --no-install-recommends -y python3 python3-pip
RUN pip3 install pynvml flask
COPY main.py main.py

ENTRYPOINT [ "python3", "main.py" ]
