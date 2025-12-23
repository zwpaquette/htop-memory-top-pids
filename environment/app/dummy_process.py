#!/usr/bin/env python3
"""Dummy process that consumes varying amounts of memory for testing."""
import time
import sys

# Allocate different amounts of memory based on instance
instance = int(sys.argv[1]) if len(sys.argv) > 1 else 0
memory_mb = [10, 20, 30, 40, 50, 60, 70, 80][instance % 8]

# Allocate memory
data = bytearray(memory_mb * 1024 * 1024)

# Keep process running
while True:
    time.sleep(60)
