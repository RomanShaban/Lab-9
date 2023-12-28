#FROM nginx:latest
FROM ubuntu

RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install flask

WORKDIR /project

COPY . /project

EXPOSE 5000

CMD python3 /project/prikol.py
