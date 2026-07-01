import pandas as pd
data= {'first':['carl', 'francis', 'sam'],
       'last': ['po','nygen', 'smith'],
       'age' : [23, 45, 43]
}
clients= pd.DataFrame(data)
print(clients)

drop_column= clients.drop(columns='first')    #removing a column
print(drop_column)

drop_row= clients.drop(index= 0)
print(drop_row)