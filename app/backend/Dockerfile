FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY . ./
RUN apt update && \
    apt upgrade -y && \
    pip3 install -U pip && \
    pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]