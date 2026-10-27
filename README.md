# tshark-live-telemetry
*(This file has been written with AI Assistance)*

A lightweight, containerized Python application that captures, filters, and analyzes live HTTP traffic in real-time using the Wireshark CLI (`tshark`).

Built to demonstrate containerization and observability principles using mock traffic.

---
## Features

- **Live Packet Capture:** Intercepts TCP traffic on port 8080 via `tshark` running inside a container.
- **Real-Time Terminal Dashboard:** Uses the Python `rich` library to render an updating telemetry grid categorized by HTTP response status codes.
- **Automated Mock Traffic Generation:** Includes a containerized daemon generating continuous HTTP traffic streams to populate the monitor.
- **Fully Containerized:** Isolated via Docker and Docker Compose for seamless deployment across environments.

---
## Tech Stack

- **Language:** Python 3, bash
- **Containerization:** Docker, Docker Compose (Debian Slim base image)
- **Networking & Security Tools:** Tshark (Wireshark CLI), cURL
- **Python Libraries:** `rich` (for stylized telemetry rendering)

---
## File Structure

```text
├── Dockerfile                  # Defines the container image and installs dependencies (Python, tshark)
├── docker-compose.yml          # Orchestrates the mock traffic server
├── code_scanner_shark.py       # Core telemetry script that parses tshark stdout and renders the UI
├── http_server.py              # Local Python HTTP server responding with randomized status codes
├── http_codes.csv              # Reference dataset mapping HTTP status codes to definitions and categories
└── mock_traffic.sh             # Bash script generating continuous randomized background traffic
```
---
## Getting Started & Installation

### Prerequisites
* Ensure you have **Docker** and **Docker Compose** installed on your system.

### Running the Project

1. **Clone the repository:**
   ```bash
   git clone https://github.com/finansminister/tshark-live-telemetry.git
   cd tshark-live-telemetry
   ```
2. **Start the mock traffic container:**
   ```bash
   docker compose up --build -d
   ```
3. **Observe the telemetry inside the terminal:**
   ```python3
   python3 code_scanner_shark.py
   ```
4. **Close down the container:**
   ```bash
   docker compose down
   ```
   Use keyboard interrupt shortcut to close down the `python` script, usually `Ctrl + C` or `Cmd + C`
