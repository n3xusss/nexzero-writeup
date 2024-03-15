FROM python:3.7
RUN pip install flask python-dotenv
COPY . /app
WORKDIR /app
RUN chown -R nobody:nogroup /app
USER nobody
EXPOSE 1337
CMD ["python3.7", "-m","flask", "run","--host=0.0.0.0", "--port=1337"]