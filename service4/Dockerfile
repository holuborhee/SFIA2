FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5003

ENTRYPOINT ["/usr/local/bin/python3", "app.py"]