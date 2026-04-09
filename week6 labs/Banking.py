class Account:
    def __init__(self,accountNumber,balance):
        self.accountNumber=accountNumber
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print(f"${amount} deposited . New balance: ${self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient fund!")
        else:
            self.balance-=amount
            print(f"{amount} has been withdrawn. New balance: {self.balance}")
    def displayBalance(self):
        print(f"Account: {self.accountNumber} \nTotal balance: ${self.balance}")

class Customer:
    def __init__(self,name,account):
        self.name=name
        self.account=account
    
    def displayCustomerInfo(self):
        print(f"Customer Name: {self.name}")
        self.account.displayBalance()


class Transaction:
    def __init__(self,account, amount, transactionType):
        self.account=account
        self.amount=amount
        self.transactionType=transactionType
        self.processTransaction()

    def processTransaction(self):
        if self.transactionType == "deposit":
            self.account.deposit(self.amount)
        elif self.transactionType == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")

account1=Account(accountNumber=101,balance=100)
customer1=Customer(name='alice', account=account1)

customer1.displayCustomerInfo()

transaction1=Transaction(account1,50,'deposit')
transaction2=Transaction(account1,30,'withdraw')

customer1.displayCustomerInfo()
