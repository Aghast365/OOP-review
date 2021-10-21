import csv

class Account:
    all_accounts = [] #class variable that holds all instances of Account
    def __init__(self, id, balance, date_opened):
        self.id = id
        self.balance = balance
        self.date_opened = date_opened


    @classmethod
    def read_from_csv(cls): #class method that gets accounts from the csv file and adds them to all_accounts
        with open("support/accounts.csv") as csv_file: 
            csv_reader = csv.DictReader(csv_file, ["id","balance","date_opened"]) #if a csv file has no fieldnames, ones can be passed as a list into DictReader
            for row in csv_reader:
                new_account = Account(**row) # the spread operator (**) allows the dict to be passed as a set of arguments
                cls.all_accounts.append(new_account) # adds the new instance of Account to the class variable

    def deposit(self, amt): #instance method that adds to the balance
        self.balance += amt
    def withdraw(self, amt): #instance method that removes from the balance
        if self.balance - amt >= 0:
            self.balance -= amt
        else:
            print("could not withdraw")



Account.read_from_csv()
#print(Account.all_accounts[0].id)

class SavingsAccount(Account): # new class that inherits from the Account class
    def __init__(self, id, balance, date_opened): #calls the init method from the Account class
        super().__init__(id, balance, date_opened)
    def withdraw(self, amt): #Overwrites the withdraw method from Account
        super().withdraw(amt + 10)


normal = Account(2, 10000, "---") #create a new instance of Account
normal.deposit(100)
normal.withdraw(100)
print("Withdraw has no fee for a normal account, so balance is: ", normal.balance)

savings = SavingsAccount(3, 10000, "---") #create a new instance of SavingsAccount
savings.deposit(100)
savings.withdraw(100)
print("Withdraw method is overridden, and now has a fee; balance is: ", savings.balance)

