#!/usr/bin/python3
"""Intialize counters"""

import sys
import signal

total_size = 0
status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

"""Function to handle CTRL+C interruption"""
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

"""Function to print statistics"""
def print_statistics():
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

"""Attach the signal handler for SIGINT (CTRL+C)"""
signal.signal(signal.SIGINT, signal_handler)

"""Read from stdin and process lines"""
try:
    for line_number, line in enumerate(sys.stdin, 1):
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        """Update total size and status code count"""
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        """Print statistics every 10 lines"""
        if line_number % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    """Handle any additional CTRL+C interruptions"""
    pass

"""Print final statistics if not a multiple of 10 lines"""
if line_number % 10 != 0:
    print_statistics()
