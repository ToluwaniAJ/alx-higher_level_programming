#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
  for r in matrix:
      for i, c in enumerate(r):
          x = ' '
          if i == len(r) - 1:
              x = ''
      print("{:d}".format(c, x), end=x)
    print("")
