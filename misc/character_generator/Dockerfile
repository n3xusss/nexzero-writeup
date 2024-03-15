FROM python:3.7-alpine

RUN apk update && \
    apk add socat 

RUN adduser --disabled-password --no-create-home ctf

COPY challenge /usr/src/app/

WORKDIR /usr/src/app

COPY ./entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN chmod +x pyjail.py

EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]
