class BankAccount:
	def __init__(self,fullname, account_number, balance):
		self.full_name=fullname
		self.account_number=account_number
		self.balance=balance
	def deposit(self,amount):
		self.balance+=amount
		print( f"amount deposited: ${amount} new balance:${self.balance}" )

	def withdraw(self,amount):
		self.balance -= amount
		print(f'amount widthdrawn: ${amount} new balance: ${self.balance}')

	def get_balance(self):
		print(f'Hello {self.full_name} your account balance is: ${self.balance}')
		return self.balance
	
	
	def add_interest(self):
		interest = 0.00083
		new_balance = interest * self.balance 
		self.balance += new_balance 
	
	def print_statement(self):
		print(f"{self.full_name} \n {self.account_number} \n {self.balance}")

Varname = BankAccount('Derek Ayala', 12345678, 0)
print(Varname.deposit(12))
print(Varname.withdraw(5))
print(Varname.get_balance())

print(Varname.print_statement())


# print(Varname.balance)


	