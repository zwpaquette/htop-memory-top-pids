# Extract Top Memory-Consuming PIDs Using htop

Your task is to launch `htop` non-interactively, apply a process name filter, sort by memory usage, and programmatically extract the top three process IDs (PIDs) to a file.

## Problem Description

The system at `/app` has multiple running processes. You need to use `htop` to filter processes by a specific name provided in `/app/process_name.txt`, sort them by memory usage in descending order, and extract the PIDs of the top three memory-consuming processes matching that filter.

## Requirements

Your solution must:

1. **Read the process name** from `/app/process_name.txt` (the file will contain a single process name to filter)
2. **Launch htop non-interactively** in batch mode to capture process information
3. **Apply a filter** for the process name read from the file
4. **Sort processes by memory usage** in descending order (highest memory first)
5. **Extract the top three PIDs** that match the filter criteria
6. **Write the PIDs** to `/app/top_pids.txt` with one PID per line, in order from highest to lowest memory usage

## Constraints

- Must use `htop` (not `top` or `ps`) to gather process information
- The solution must work non-interactively (no manual user interaction)
- If fewer than three processes match the filter, write only the PIDs that exist
- If no processes match the filter, create an empty `/app/top_pids.txt` file
- PIDs must be written as plain integers, one per line, no additional text or formatting
- Must handle cases where the process name filter matches multiple processes

## Files

- Input: `/app/process_name.txt` (contains the process name to filter)
- Output: `/app/top_pids.txt` (contains up to 3 PIDs, one per line, sorted by memory usage descending)

## Success Criteria

1. `/app/top_pids.txt` exists and contains valid PIDs
2. PIDs are sorted by memory usage (highest memory first)
3. Maximum of three PIDs are listed
4. Each PID corresponds to a process matching the filter from `/app/process_name.txt`
5. The solution works non-interactively without requiring user input
