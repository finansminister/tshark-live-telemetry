FROM debian:stable-slim

WORKDIR /app

RUN apt-get update && apt-get install -y python3 curl tshark

COPY http_server.py /app/http_server.py
COPY http_codes.csv /app/http_codes.csv

CMD ["python3", "-u", "http_server.py"]
