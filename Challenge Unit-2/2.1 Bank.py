class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      # self.__account_balance = self.__account_balance+amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount,
                                                     self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      # self.__account_balance = self.__account_balance - amount
      print("Withdrew ₹{}. New balance: ₹{}".format(amount,
                                                    self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))
# Create an instance of the BankAccount class
account = BankAccount(account_number=int(input("Enter the account number: ")),
                      account_holder_name=str(input("Enter the account holder name: ")),
                      initial_balance=int(input("Enter the initial balance: ")))
# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(amount=int(input("Enter the amount to deposit: ")))
account.withdraw(amount=int(input("Enter the amount to withdraw: ")))
account.withdraw(amount=int(input("Enter the amount to withdraw: ")))
account.display_balance()