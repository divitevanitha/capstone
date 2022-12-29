class NegativeValueError(Exception):
    pass
class HighAmountError(Exception):
    def __str__(self):
        return "deposit ammount can't be greater than 10000"
class bank_account:
    def __init__(self,name,account_num,available_balance):
        self.name=name
        self.account_num=account_num
        self.available_balance=available_balance
    def avail_balance(self):
        print("available balance",self.available_balance)
    def withdraw(self,withdraw_amount):
        try:
            self.withdraw_amount=withdraw_amount
            print("withdraw amount is",self.withdraw_amount)
            if self.withdraw_amount < self.available_balance:
                self.available_balance = self.available_balance - withdraw_amount
                print("amount is withdrawn",self.available_balance)
            else:
                raise NegativeValueError
        except NegativeValueError:
            print("insufficient balance")
    def deposit(self,deposit_amount):
        print('deposit amount is',self.deposit_amount)
        try:
            if deposit_amount > 10000:
                raise HighAmountError
            else:
                self.available_balance=self.available_balance+deposit_amount
                print(self.available_balance)
        except HighAmountError as h:
            print(h)


obj= bank_account("vanitha",12345678,1000)
obj.avail_balance()
obj.withdraw(1001)
obj.avail_balance()
obj.deposit(19999)
obj.avail_balance()


