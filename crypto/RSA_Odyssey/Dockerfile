FROM python:3-alpine
RUN apk update && apk add socat
RUN adduser -D ctf
WORKDIR /app
COPY . /app
RUN chown -R ctf:ctf /app
RUN pip3 install --no-cache-dir pycryptodome
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chown ctf:ctf /entrypoint.sh
EXPOSE 1337
ENTRYPOINT ["/entrypoint.sh"]
