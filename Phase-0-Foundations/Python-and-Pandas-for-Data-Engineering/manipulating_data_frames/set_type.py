import pandas as pd
data= {'first':['carl', 'francis', 'sam'],
       'last': ['po','nygen', 'smith'],
       'age' : [23, 45, 43]
}
clients= pd.DataFrame(data)
print(clients)
 
age= clients.age 
print(age)  