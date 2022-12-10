#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
  for row in matrix:
      for i, c in enumerate(row):
          x = ' '
          if i == len(row) - 1:
              x = ''
      print("{:d}".format(c, x), end=x)
    print("")
