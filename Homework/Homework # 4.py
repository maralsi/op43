
# Базовые классы
class Asset:
    pass

class InsurableItem:
    pass

class InterestBearingItem:
    pass

# Производные классы
class BankAccount(Asset):
    pass

class SavingAccount(BankAccount, InterestBearingItem):
    pass

class CheckingAccount(BankAccount):
    pass

class RealEstate(Asset, InsurableItem):
    pass

class Security(Asset):
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass
