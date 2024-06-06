
class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount
        print(f"На счет добавлено {amount}. Новый баланс: {self._balance}")

    def _kill(self):
        self._balance = 0
        print(f"Баланс обнулен. Новый баланс: {self._balance}")

    def __jackpot(self):
        self._balance *= 10
        print(f"Поздравляем! Ваш баланс увеличен в 10 раз. Новый баланс: {self._balance}")

    def _merge_balance(self, other):
        self._balance += other._balance
        print(f"Баланс объединен. Новый баланс: {self._balance}")

bank1 = Bank("Клиент1", 1000)
bank2 = Bank("Клиент2", 2000)

bank1.moneyX()  # Вводим сумму, например, 500
bank1._kill()
bank1._merge_balance(bank2)

# Для доступа к скрытому методу __jackpot используем манипуляции с именем
bank1._Bank__jackpot()


class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        else:
            return Calculator(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        else:
            return Calculator(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        else:
            return Calculator(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value / other.value)
        else:
            return Calculator(self.value / other)

    def __str__(self):
        return str(self.value)

calc1 = Calculator(10)
calc2 = Calculator(5)

calc3 = calc1 + calc2
calc4 = calc1 - calc2
calc5 = calc1 * calc2
calc6 = calc1 / calc2

print(calc3)  # Output: 15
print(calc4)  # Output: 5
print(calc5)  # Output: 50
print(calc6)  # Output: 2.0

