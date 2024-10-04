#!/usr/bin/python3

def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's Triangle of size n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        """
        Create the current row with 1 at the beginning and end,
        and use list comprehension to generate the middle elements.
        """
        row = [1] + [triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle
