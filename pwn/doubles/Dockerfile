FROM ubuntu:18.04

RUN apt update \
    && apt install -y socat

RUN useradd ctf && \
    mkdir /challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chown -R root:root . && \
    chmod +x chall ld.so.2 libc.so.6

EXPOSE 1337

ENTRYPOINT [ "./entrypoint.sh" ]

