class ATM:
    def __init__(self):
        self.banknotes = [0, 0, 0, 0, 0]
        self.denominations = [10, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        if len(banknotesCount) != 5:
            print("Error: banknotesCount.length must be 5")
            return
        for count in banknotesCount:
            if not (0 <= count <= 10**9):
                print("Error: Each banknote count must be between 0 and 10^9")
                return

        for i in range(5):
            self.banknotes[i] += banknotesCount[i]
        return "void"

    def withdraw(self, amount):
        if not (1 <= amount <= 10**9):
            print("Error: Amount must be between 1 and 10^9")
            return [-1]

        original_banknotes = self.banknotes[:]
        result = [0] * 5
        for i in range(4, -1, -1):
            if amount >= self.denominations[i]:
                count = min(amount // self.denominations[i], self.banknotes[i])
                amount -= count * self.denominations[i]
                result[i] = count

        if amount == 0:
            for i in range(5):
                self.banknotes[i] -= result[i]
            return result
        else:
            self.banknotes = original_banknotes
            return [-1]

# Тесты
obj = ATM()
print(f"obj.deposit([0, 0, 1, 2, 1]) -> {obj.deposit([0, 0, 1, 2, 1])}")
param_2 = obj.withdraw(600)
print(f"obj.withdraw(600) -> {param_2}")
print(f"obj.deposit([0, 1, 0, 1, 1]) -> {obj.deposit([0, 1, 0, 1, 1])}")
param_2 = obj.withdraw(600)
print(f"obj.withdraw(600) -> {param_2}")
param_2 = obj.withdraw(550)
print(f"obj.withdraw(550) -> {param_2}")
print(f"obj.deposit([0, 0, 2, 1, 1]) -> {obj.deposit([0, 0, 2, 1, 1])}")
param_2 = obj.withdraw(700)
print(f"obj.withdraw(700) -> {param_2}")

print(f"obj.withdraw(0) -> {obj.withdraw(0)}")
try:
    obj.deposit([0, 0, 1, 2])
except Exception as e:
    print(f"Error: {e}")

obj = ATM()
obj.deposit([1, 1, 1, 1, 1])
print(f"obj.withdraw(1000) -> {obj.withdraw(1000)}")