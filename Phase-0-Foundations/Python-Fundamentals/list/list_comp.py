number=[1,2,3,4,5,6,7,8,9]
squares=[i*i for i in number]
print(squares) 

even=[i for i in number if i%2==0]
print (even)

names=["abdullah", "at", "tarik"]
upper= [names.upper() for names in names]
print(upper)

data=[("abc",80), ("def",75), ("ghi",95)]
codes, marks = zip(*data) 
print(codes) 
print(marks)