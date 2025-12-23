"""Tests for htop process filtering and PID extraction task."""
import subprocess
from pathlib import Path


def test_top_pids_file_exists():
    """Verify that /app/top_pids.txt file was created."""
    output_file = Path("/app/top_pids.txt")
    assert output_file.exists(), "/app/top_pids.txt file does not exist"


def test_top_pids_file_not_empty():
    """Verify that /app/top_pids.txt contains at least one PID."""
    output_file = Path("/app/top_pids.txt")
    content = output_file.read_text().strip()
    assert len(content) > 0, "/app/top_pids.txt is empty"


def test_top_pids_contains_valid_integers():
    """Verify that all PIDs in the file are valid integers."""
    output_file = Path("/app/top_pids.txt")
    lines = output_file.read_text().strip().split('\n')
    
    for line in lines:
        if line.strip():  # Skip empty lines
            try:
                pid = int(line.strip())
                assert pid > 0, f"PID {pid} must be positive"
            except ValueError:
                assert False, f"Line '{line}' is not a valid integer PID"


def test_maximum_three_pids():
    """Verify that at most three PIDs are listed in the file."""
    output_file = Path("/app/top_pids.txt")
    lines = [line.strip() for line in output_file.read_text().strip().split('\n') if line.strip()]
    
    assert len(lines) <= 3, f"Found {len(lines)} PIDs, expected maximum 3"


def test_pids_correspond_to_running_processes():
    """Verify that each PID in the file corresponds to an actual running process."""
    output_file = Path("/app/top_pids.txt")
    lines = output_file.read_text().strip().split('\n')
    
    for line in lines:
        if line.strip():
            pid = int(line.strip())
            
            # Check if process exists
            result = subprocess.run(
                ['ps', '-p', str(pid)],
                capture_output=True,
                text=True
            )
            
            assert result.returncode == 0, f"PID {pid} is not a running process"


def test_pids_match_filtered_process_name():
    """Verify that PIDs belong to processes matching the filter from process_name.txt."""
    process_name_file = Path("/app/process_name.txt")
    assert process_name_file.exists(), "/app/process_name.txt does not exist"
    
    process_name = process_name_file.read_text().strip()
    output_file = Path("/app/top_pids.txt")
    lines = output_file.read_text().strip().split('\n')
    
    for line in lines:
        if line.strip():
            pid = int(line.strip())
            
            # Get process command
            result = subprocess.run(
                ['ps', '-p', str(pid), '-o', 'comm='],
                capture_output=True,
                text=True
            )
            
            process_cmd = result.stdout.strip()
            assert process_name in process_cmd, (
                f"PID {pid} has command '{process_cmd}' which does not match filter '{process_name}'"
            )


def test_pids_sorted_by_memory_descending():
    """Verify that PIDs are sorted by memory usage in descending order."""
    output_file = Path("/app/top_pids.txt")
    lines = [line.strip() for line in output_file.read_text().strip().split('\n') if line.strip()]
    
    if len(lines) < 2:
        return  # Can't test sorting with less than 2 PIDs
    
    memory_values = []
    for line in lines:
        pid = int(line.strip())
        
        # Get memory usage (RSS) for this PID
        result = subprocess.run(
            ['ps', '-p', str(pid), '-o', 'rss='],
            capture_output=True,
            text=True
        )
        
        rss = int(result.stdout.strip())
        memory_values.append(rss)
    
    # Check that memory values are in descending order
    for i in range(len(memory_values) - 1):
        assert memory_values[i] >= memory_values[i + 1], (
            f"PIDs not sorted by memory: {memory_values[i]} KB < {memory_values[i+1]} KB"
        )


def test_process_name_file_exists():
    """Verify that /app/process_name.txt exists as input."""
    process_name_file = Path("/app/process_name.txt")
    assert process_name_file.exists(), "/app/process_name.txt does not exist"


def test_one_pid_per_line():
    """Verify that each line contains exactly one PID with no extra formatting."""
    output_file = Path("/app/top_pids.txt")
    lines = output_file.read_text().strip().split('\n')
    
    for line in lines:
        if line.strip():
            # Check that line is just a number, no extra text
            parts = line.strip().split()
            assert len(parts) == 1, f"Line '{line}' should contain only one PID"
            
            # Verify it's a valid integer
            try:
                int(parts[0])
            except ValueError:
                assert False, f"Line '{line}' does not contain a valid integer"


def test_all_pids_are_unique():
    """Verify that all PIDs in the output are unique (no duplicates)."""
    output_file = Path("/app/top_pids.txt")
    lines = [line.strip() for line in output_file.read_text().strip().split('\n') if line.strip()]
    
    pids = [int(line) for line in lines]
    unique_pids = set(pids)
    
    assert len(pids) == len(unique_pids), (
        f"Found duplicate PIDs in output: {pids}"
    )
