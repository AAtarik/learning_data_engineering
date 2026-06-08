allowed_users = ["manager", "staff", "officer"]

user = input("enter your role: ")

print(user in allowed_users)