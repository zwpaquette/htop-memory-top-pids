#!/bin/bash
# Start multiple dummy python3 processes with different memory usage

python3 /app/dummy_process.py 5 &  # 60 MB - highest
python3 /app/dummy_process.py 4 &  # 50 MB - second
python3 /app/dummy_process.py 3 &  # 40 MB - third
python3 /app/dummy_process.py 2 &  # 30 MB
python3 /app/dummy_process.py 1 &  # 20 MB - lowest

# Give processes time to allocate memory
sleep 3

echo "Started 5 python3 processes with varying memory usage"
