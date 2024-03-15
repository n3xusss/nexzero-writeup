FROM python:3.10-alpine

RUN apk update && \
    apk add socat && \
    apk add sqlite && \
    apk add vim

RUN adduser --disabled-password --no-create-home ctf

COPY challenge /usr/src/app/

WORKDIR /usr/src/app

RUN chmod 444 ./flag.txt
RUN chmod 444 ./challenge.py

RUN chmod +x ./entrypoint.sh

RUN chmod +x ./challenge.py

RUN cp /usr/bin/vim /bin/vim

EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]
