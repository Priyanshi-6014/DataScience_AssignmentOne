from random import random

l = [random() for i in range(20)]    # defining  list
x = random()

sort_l = sorted(l)                   # sorting list, here list will be sorted in ascending order
print(sort_l)
print(x)


count = 0
while sort_l[count] < x:            # while loop will continue till numbers in sorted list is smaller than x
    count += 1                      # count will get bigger by 1 as long as while condition is true, here count is number of index.

print(count)                        # as soon as we find number which is greater or equal to x, while will stop and,
                                    # we will get index of the number that is greater or equal to x.


