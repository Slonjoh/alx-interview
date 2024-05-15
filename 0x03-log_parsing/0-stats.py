#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
valid_codes = set(status_codes.keys())
line_count = 0


def print_stats():
    """ Print the accumulated metrics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """ Handle keyboard interruption """
    print_stats()
    sys.exit(0)


# Set up signal handler for keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            ip = parts[0]
            date = parts[3] + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        if request != "\"GET /projects/260 HTTP/1.1\"":
            continue

        # Update metrics
        total_size += file_size
        if status_code in valid_codes:
            status_codes[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final stats if EOF is reached
print_stats()
