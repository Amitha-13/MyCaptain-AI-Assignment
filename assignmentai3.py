# -*- coding: utf-8 -*-
"""AssignmentAI3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kPHb41w3V1DjSOwG8TeIJHQ7Kx-bnRYE
"""

def print_posnum(input_list):
    #filter out positive numbers from the list
    posnum= [num for num in input_list if num>0]
    return posnum

#example input lists
list1 = [14, -8, 45, -34, -22]
list2 = [6, -84, 24, 9]

#output for list1
print("output:", print_posnum(list1))

#output for list2
print("output:", print_posnum(list2))