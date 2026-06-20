class BankAccount():
    def __init__(self, name, balance):
        self.__balance = balance                 #double underscore dile private variable hoye jbe.
                                                  # balance direct change krte parbe nh, deposit /withdraw krte hbe
        self.name = name 
    def deposit(self, amount):
        if amount>0:
         self.__balance +=amount
    def withdraw(self, amount):
       if 0<amount <= self.__balance:
        self.__balance -= amount 
       else :
          print("in-valid withderaw")

    def get_balance(self):
       return self.__balance 

acc1= BankAccount("Tarik", 10000)

print("1st", acc1.get_balance())
acc1.deposit(5000)
print("After deposit 5000 :", acc1.get_balance())
acc1.withdraw(2000)
print("after withdraw 2000 :", acc1.get_balance())