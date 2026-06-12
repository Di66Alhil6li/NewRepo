class AccountBank:
    withdrawal_limit = 1000000.00
    minimum_balance = 1000.00
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_log = []


    def deposit(self, amount):        
        self.balance += amount
        self.transaction_log.append(("+"+str(amount), " Deposited"))
    
    def withdraw(self, amount):
        if amount <= AccountBank.withdrawal_limit :
            if amount <= self.balance and  amount >= AccountBank.minimum_balance:
                self.balance -= amount
                self.transaction_log.append((amount * -1, " Withdrawn"))
            else:
                print(f"Insufficient balance. Current balance: {self.balance:.2f}")
        else:
            print(f"Withdrawal amount exceeds the limit of {AccountBank.withdrawal_limit:.2f}.")

    def show_output(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance:.2f}")
        print("Transaction Log:")
        for transaction in self.transaction_log:
            print(transaction)

# Example usage
# account = AccountBank("John Doe", 50000.00)
# account.deposit(10000.00)
# # account.withdraw(5000.00)
# account.show_output()

# user = AccountBank("Alice", 300000.00)
# user.deposit(5000.00)

# q = account.transaction_log

# print(q)


# v = user.balance
# print(v)
# user.withdraw(20000.00)
# user.deposit(10000.00)
# user.show_output()

# vs = user.transaction_log
# print(vs)

sd = {"name":["ss","ff","dd"],
    "age": [11,22,33]}

lf =sd["name"].index("ss")
d = sd["name"][[lf].pop(lf)]
c = sd["age"][[lf].pop(lf)]


for i in sd.values():
    for j in i:
        if j == "ss":
            print(j)

print(lf)
print(d)
print(c)
print(sd)