def list_of_string(*string):  # Here * is used so that we can take inputs of list

    for name in string:       #using for function, now "string" is stored in "name"
        value = len(name)    #Assigning lenght of element to the value variable so that it can be easy afterwards to call it.
        print(f'{name} : {value} ')




