def check_result(n):
    if (n>=40):
        return "Pass"
    else:
        return "Fail"
    
n= int (input("enter marks: "))
result= check_result (n)
print(result)