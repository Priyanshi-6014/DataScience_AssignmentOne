import math

result = 1
i = 0
while result < 10**8:       # as we want result to be greater than or equal to 10^8,
    result = i*(i+1)
    i += 1
print(result)
