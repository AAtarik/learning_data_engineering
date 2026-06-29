import pandas as pd
file_path ='USCG.Search.Rescue.Stats.csv'     #for example, file doesn't exists 
df= pd.read_csv(file_path)  
print (df) 

df.head(3)    #it will show top 3 row of the file

df.tail(3)    #it will show last 3 row of the file

df.describe() #it will the statistics of the file

df.columns
df['Cases']    # this will show the data of the column named "Cases". u can use multiple column by using [] this bracket

df.iloc[3:29, 3] 
""" [3:29] eti row er index number-(row 3 hotee 29 porjonto data show krbe) & 
                 [ , 3] eti ei index er column er data show krbe"""

df.loc[3:20, 'Cases']
""" 3no row hote 20no row er "Cases" column er data show krbe  (ei khetre row number ar column er naam 
use krte hbe)"""
                            