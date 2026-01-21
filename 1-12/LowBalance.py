class LowBalanceError(Exception):
    pass
Bal = 1000000
def withdraw(amount,Balance = Bal):
    if amount > Balance:
        raise LowBalanceError("Balance is insufficient")
    else:
        Balance -= amount

withdraw(50000000)