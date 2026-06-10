ages=[1,2,3,4,5,6]
ages.append(8)
print(ages)
ages.append("Yes")
print(ages)
new_ages=[10,15,19,17]
ages.append(new_ages)
print(ages)

#extend
print("EXTEND")
list=[1,2,3,4,5]
new_list=[6,7,8,9]
list.extend(new_list)
print(list)

#insert
print ("INSERT")        #nirdishto index e notun element add kra
nums=[10,20,40,50]
nums.insert(2,30)
print(nums)

#remove
print("REMOVE")
num_word=[1,2,3,4,5,"a","b","c"]
num_word.remove("a")          #jeta remove krbo sheta bracket er bhitor
print(num_word)

#pop
print("POP")
x=[10,20,30,40,50]
y= x.pop(2)                    #pop(index)
print (x)
print(y)

#sort
print("SORT")
z=['a', 'f', 'd', 'e', 'b','c']
z.sort()
print(z)
marks=[100,200,80,500,38]      #choto theke boro shajanu
marks.sort()
print(marks)
marks.sort(reverse=True)       #boro theke choto
print(marks)

#count
print("COUNT")
x=[1,2,3,3,3,3,2,2,9,5,9,9,5,]
print(x.count(3))