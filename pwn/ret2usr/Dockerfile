FROM ubuntu:18.04

RUN apt update \
    && apt install -y socat python3 procps qemu-system-x86

RUN useradd ctf && \
    mkdir /challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chown -R root:root . && \
    chmod +x  entrypoint.sh

USER ctf
EXPOSE 80

ENTRYPOINT [ "./entrypoint.sh" ]
