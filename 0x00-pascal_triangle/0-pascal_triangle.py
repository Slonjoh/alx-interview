#!/usr/bin/python3
"""
A function that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                """Edges are always 1 """
                row.append(1)
            else:
                """
                Elements derived 4rm d sum of d 2 elements above them
                """
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
