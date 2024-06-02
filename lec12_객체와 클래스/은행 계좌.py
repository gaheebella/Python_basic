class Account:
    def __init__(self, balance=0):
        self.__balance = balance

    def withdraw(self, amount):
        self.__balance -= amount
        print(f"통장에서 {amount}가 출금되었음")
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"통장에 {amount}가 입금되었음")
        return self.__balance

money = Account()
money.withdraw(100)
money.deposit(10)
