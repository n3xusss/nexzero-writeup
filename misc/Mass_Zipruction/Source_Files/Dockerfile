FROM python:3-alpine

RUN apk update && \
    apk add socat && \
    apk add zip

RUN apk add --no-cache dcron
RUN echo "0 * * * * /bin/rm -rf /tmp/temp*" > /etc/crontabs/root

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /challenge/

COPY ./server.py ./
COPY ./flag.txt /flag.txt

RUN rm -rf /challenge/books/
RUN mkdir /challenge/books/ && \
    chmod 777 /challenge/books/ && \
    chmod 666 /flag.txt

EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]
