number = int(input("Enter total amount :"))
if number >= 5000:
    print("eligible for discount")
    print("enter mode of payment")
    mode = input("A-cash B-card C-UPI :")
    if mode == "B":
      print("discount applied ")
    elif mode == "A" or mode == "C":
      print("discount not applied")
    else:
      print("in-valid")

elif number > 0 and number < 5000:
    print("not eligible ")
else:
    print("please do shopping")
