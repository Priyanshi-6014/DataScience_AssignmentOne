import pandas as pd                                    # importing package



data = dict(A=[1,2,2,1],
        B= [3.1, 4.2, 1.5, 6.3],
        C= [800,150,400,210])


df = pd.DataFrame(data)   # calling function to form a data frame, with index not default.
print(df)



