FROM python:3.6-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev sudo


# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel


# RUN adduser docker && echo "docker:docker" | chpasswd && adduser docker sudo

# USER docker
# CMD /bin/bash

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

RUN chmod 777 /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
