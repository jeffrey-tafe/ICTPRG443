class Account:
    def __init__(self, new_id, balance, annual_interest_rate):
        self.__id = new_id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def get_annual_interest_rate(self):
        return self.__annual_interest_rate

    def set_id(self, new_id):
        self.__id = new_id

    def set_balance(self, balance):
        self.__balance = balance

    def set_annual_interest_rate(self, rate):
        self.__annual_interest_rate = rate

    def get_monthly_interest_rate(self):
        return (self.__annual_interest_rate / 100) / 12

    def get_monthly_interest(self):
        return self.__balance * self.get_monthly_interest_rate()

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        details = f"\nID: {self.__id}"
        details += f"\nBalance: {self.__balance}"
        details += f"\nAnnual Interest Rate: {self.__annual_interest_rate}"
        details += f"\nMonthly Interest Rate: {self.get_monthly_interest_rate()}"
        details += f"\nMonthly Interest: {self.get_monthly_interest()}"
        return details
