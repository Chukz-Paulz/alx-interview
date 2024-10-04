#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    This Returns a list of lists of integers representing Pascal's Triangle of size n.
    Will Return an empty list if n <= 0.
    """
    q = []
    if n <= 0:
        return q

    q = [[1]]
    for i in range(1, n):
        """
        This Create a new row starting with 1,
        and compute the values by summing adjacent elements from the previous row.
        """
        temp = [1]
        for j in range(len(q[i - 1]) - 1):
            curr = q[i - 1]
            temp.append(curr[j] + curr[j + 1])
        temp.append(1)
        q.append(temp)

    return q
