


def proportion (mylist, item):  # defining a function that counts proprotion of each item in the list.
    count =0
    for x in mylist:
        if x<=int(item):         # will count how many numbers are smaller than or equal to that number in the list.
            count+=1
    return(round(count/len(mylist),2))      # divide by length of list to give proprotion




def gives_dictionary(*list):         # function that will return dictionary with key value pairs  of number and its proportion
    for x in list:
     print(f'{x} : {proportion(list,x)}')






