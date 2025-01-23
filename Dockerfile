FROM python:3.12-slim-buster

WORKDIR /usr/src/app

RUN pip install requests pygithub

COPY . .

CMD ["python", "app.py"]
