FROM debian:stable-slim

WORKDIR /app

RUN apt-get update && apt-get install -y python3 curl tshark

COPY http_server.py /app/http_server.py
COPY http_codes.csv /app/http_codes.csv
<<<<<<< HEAD

CMD ["python3", "-u", "http_server.py"]
=======
COPY mock_traffic.sh /app/mock_traffic.sh

RUN chmod +x /app/mock_traffic.sh

CMD ["sh", "-c", "python3 -u http_server.py & ./mock_traffic.sh"]
>>>>>>> 9e0615d (initial commit)
