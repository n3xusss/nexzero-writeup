FROM node:18.16.0-alpine3.17

COPY . /app
WORKDIR /app
RUN npm install

EXPOSE 3000

ENTRYPOINT ["npm", "start"]

