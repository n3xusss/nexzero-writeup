FROM ubuntu:18.04

RUN apt update \
    && apt install -y socat 

RUN mkdir /challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x  chall entrypoint.sh

EXPOSE 3000

ENTRYPOINT [ "./entrypoint.sh" ]
