FROM ubuntu:22.04

WORKDIR /app

# Install system dependencies including htop
RUN apt-get update && apt-get install -y \
    htop=3.0.5-7build2 \
    procps \
    python3 \
    && rm -rf /var/lib/apt/lists/*

# Create dummy processes for testing
COPY app/ /app/

# Set environment
ENV TERM=xterm
