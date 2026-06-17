class BankAccount():
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name 
        
acc1= BankAccount("Tarik", 10000)
print(acc1.name)