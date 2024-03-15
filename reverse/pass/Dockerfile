FROM alpine:latest

RUN apk update && apk add socat python3 
COPY challenge /challenge

WORKDIR /challenge



RUN chmod +x entrypoint.sh pass  && \
    chown -R root:root .
    
EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]
