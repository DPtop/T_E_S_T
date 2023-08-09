class Wallet:
    def __init__(self, balance:int=0):
        self.__balance = balance
        self.__check_balance_zero = 0

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
        return str(self.balance)

    def __sub__(self, other):
        sub = Wallet(self.__balance - other.balance)
        return sub if str(sub) >= str(self.__check_balance_zero) else 'будет меньше нуля...'


wallet1 = Wallet(100500)
wallet2 = Wallet(100499)
wallet3 = Wallet(100500)
wallet4 = Wallet(100501)

print(wallet1 - wallet2)
print(wallet1 - wallet3)
print(wallet1 - wallet4)

