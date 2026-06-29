import pandas as pd 
data =[['Carl', 123, 43],
       ['Carol', 234, 44],
       ['Cas', 567, 45]
]
df= pd.DataFrame(data, columns=['Name','run', 'Age'])
print(df)