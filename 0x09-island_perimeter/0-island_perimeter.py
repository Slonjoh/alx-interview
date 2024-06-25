#!/usr/bin/python3
"""
Module: 0-island_perimeter

Contains a function to determine the perimeter of
an island described in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
    - grid (list of list of int): The grid representing the island and water.

    Returns:
    - int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four sides
                # Top
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Bottom
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
