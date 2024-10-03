#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        # Generate the middle elements by summing the previous row elements
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

# Testing the function using the provided `print_triangle` function
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
