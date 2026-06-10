import copy 

x=[1,2,3,[4,5]]
y= copy.deepcopy(x)
y[3].append(6)
print(x)
print(y)