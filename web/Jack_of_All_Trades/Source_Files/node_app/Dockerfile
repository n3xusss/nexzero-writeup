FROM node:18.16.0-alpine3.17

RUN apk add socat
COPY . /app
WORKDIR /app
RUN npm install

EXPOSE 3000

ENTRYPOINT ["node", "app.js"]
