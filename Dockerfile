# Video Downloader — Docker image (for the free Render deploy)
# ffmpeg is required, so Docker is used: Render's plain Python
# environment does not include ffmpeg, but it can be installed
# here with apt.
FROM python:3.12-slim

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# server.py reads the PORT environment variable itself (Render provides it)
CMD ["python", "server.py"]
