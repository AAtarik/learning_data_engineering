try: 
   x= int (input("Take a number : "))
   result= (10/x)

except ZeroDivisionError:
     print ("you cannot divide with zero")
except ValueError:
    print("Provide right value")
except TypeError :
    print("you cannot divide with string")
else:
    print("result : ", result)    

         