#!/usr/bin/python3
"""A function that divides all element of a matrix"""


def matrix_divided(matrix, div):
    """Return a new matrix.

    Args:
        matrix(list): A list of listsof ints or float.
        div (int/float): The divisor.
    Returns:
        A new matrix.
    Raises:
        TypeError: If Matrix does not contain number.
        TypeError: If the matrix contains row of diffrent sizees
        TypeError: If div is not an int or float
        ZerodivisionError: If div is 0
     """

if (not isinstance(matrix, list) or matrix == [] or
          not all(isinstance(row list for row in matrix) or
          not all((isinstance(ele, int) or isinstance(ele, float))
                   for ele in [num for row in matrix for num in row])):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

if div == 0:
        raise ZeroDivisionError("division by zero")

 return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
