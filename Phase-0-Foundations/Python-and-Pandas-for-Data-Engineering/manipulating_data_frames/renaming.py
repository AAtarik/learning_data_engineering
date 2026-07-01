import pandas as pd
data= {'first':['carl', 'francis', 'sam'],
       'last': ['po','nygen', 'smith'],
       'age' : [23, 45, 43]
}
clients= pd.DataFrame(data)
print(clients)

column_update= clients.rename(columns={'first':'First name'})    
print(column_update)

row_no_update= clients.rename(index={0:'a', 1:'b', 2:'c'})
print(row_no_update)