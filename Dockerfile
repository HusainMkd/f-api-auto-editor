FROM python:3.8-slim-buster
WORKDIR /app
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN pip install --upgrade pip
RUN pip install auto-editor

COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt

COPY fastapiapp.py /app
WORKDIR /app
EXPOSE  80
CMD [ "uvicorn", "fastapiapp:app", "--host", "0.0.0.0", "--port", "80" ]
# ENTRYPOINT /usr/local/bin/gunicorn -b 0.0.0.0:80 -w 4 -k uvicorn.workers.UvicornWorker fastapiapp:app --chir /app
# Docker build command: docker build --tag auto-editor-docker2:v1.5 . 
# Docker rename latest build: docker tag auto-editor-docker2:v1.5 auto-editor-docker2:latest
# Docker command: docker run -it -d -p 80:80 --name auto-editor-docker2 auto-editor-docker2 