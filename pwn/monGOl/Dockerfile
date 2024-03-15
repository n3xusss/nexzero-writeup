FROM ubuntu:latest

RUN apt update \
    && apt install -y socat

RUN useradd ctf && \
    mkdir /challenge

COPY chall /challenge

WORKDIR /challenge

RUN chown -R root:root . && \
    chmod +x  monGOal entrypoint.sh && \
    chmod +r flag.txt
	

EXPOSE 1337

ENTRYPOINT [ "./entrypoint.sh" ]

