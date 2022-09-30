def exponential(x, y):    # function which takes x and y as a argument
    result = pow(x,y)       # performing math operation
    print(result)         # will print the result


l = [[5, 6], [5, 7], [4, 2], [3, 6], [9, 8], [1, 3], [9, 3], [7, 1], [5, 4], [2, 7], [9, 1], [9, 3], [2, 5]]

for numbers in l:
     exponential(numbers[0], numbers[1])  # calling the function to perform operation on l.
