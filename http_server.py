import csv
import http.server
import random
from typing import Any

codes = []
with open("http_codes.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        code = int(row["Code"]) # code value from http_codes.csv
        codes.append(code)

class TrafficHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        random_code = random.choice(codes)
        self.send_response(random_code)
        self.end_headers()
        self.wfile.write(f"HTTP Code: {random_code}\n".encode())

    def log_message(self, format: str, *args: Any) -> None:
        return

if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", 8080), TrafficHandler)
    server.serve_forever()
