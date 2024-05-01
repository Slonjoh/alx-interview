#!/usr/bin/python3
"""
Determine if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    :param boxes: List of lists. Each inner list contains the keys for the
    corresponding box.
    :return: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False  # No boxes to unlock

    n = len(boxes)
    opened = set()  # Set of opened boxes
    keys = set([0])  # We start with the key to the first box

    # Use a stack to simulate a depth-first search
    stack = [0]  # We start by unlocking the first box

    while stack:
        current_box = stack.pop()  # Get the last box in the stack
        if current_box not in opened:
            opened.add(current_box)  # Mark the box as opened
            # Add the keys found in this box to our keys set
            keys.update(boxes[current_box])
            # Add the new keys to the stack for further exploration
            for key in keys:
                if key < n and key not in opened:
                    stack.append(key)

    # If we've opened all boxes, return True
    return len(opened) == n
