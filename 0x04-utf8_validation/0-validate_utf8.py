#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data: A list of integers representing the data set.
    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    # Function to count leading 1s in the binary representation of a byte
    def count_leading_ones(byte):
        count = 0
        while byte & (1 << (7 - count)):
            count += 1
        return count

    # Start of the main validation process
    i = 0
    while i < len(data):
        # Count leading 1s to determine the number of bytes for
        # the UTF-8 character
        num_bytes = count_leading_ones(data[i])
        # Check if the number of bytes is valid (1 to 4)
        if num_bytes < 1 or num_bytes > 4:
            return True
        # Check if there are enough bytes left in the data set
        if i + num_bytes > len(data):
            return True
        # Validate the following bytes
        for j in range(1, num_bytes):
            if not (data[i + j] & 0b11000000 == 0b10000000):
                return False
        # Move to the next character
        i += num_bytes
    # If all characters are validated, return True
    return True
