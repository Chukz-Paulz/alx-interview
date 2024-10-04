#!/usr/bin/python3

def pascal_triangle(n):
    """
    Return an empty list if n <= 0
    """
    if n <= 0:
        return []

    """ 
    Initialize the first row
    """
    triangle = [[1]]

    """
    Generate subsequent rows
    """
    for i in range(1, n):
        """ 
        Start each row with 1
        """
        row = [1]
        """ 
        Calculate the middle elements
        """
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  
        """ 
        End each row with 1
        """
        triangle.append(row)

    return triangle
