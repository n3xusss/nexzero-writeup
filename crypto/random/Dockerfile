FROM python:3.9.18-alpine3.18

RUN apk update && apk add socat

RUN adduser --disabled-password --no-create-home ctf

COPY --chown=ctf:ctf chall /chall

WORKDIR /chall

ENTRYPOINT ["./entrypoint.sh"]
