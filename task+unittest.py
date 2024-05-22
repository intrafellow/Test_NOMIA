import unittest


class ATM:
    def __init__(self):
        self.banknotes = [0, 0, 0, 0, 0]
        self.denominations = [10, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        if len(banknotesCount) != 5:
            return "Error: banknotesCount.length must be 5"
        for count in banknotesCount:
            if not (0 <= count <= 10**9):
                return "Error: Each banknote count must be between 0 and 10^9"

        for i in range(5):
            self.banknotes[i] += banknotesCount[i]
        return "void"

    def withdraw(self, amount):
        if not (1 <= amount <= 10**9):
            return "Error: Amount must be between 1 and 10^9"

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


class TestATM(unittest.TestCase):

    def test_deposit_and_withdraw(self):
        obj = ATM()
        self.assertEqual(obj.deposit([0, 0, 1, 2, 1]), "void")
        self.assertEqual(obj.withdraw(600), [0, 0, 1, 0, 1])

        self.assertEqual(obj.deposit([0, 1, 0, 1, 1]), "void")
        self.assertEqual(obj.withdraw(600), [-1])
        self.assertEqual(obj.withdraw(550), [0, 1, 0, 0, 1])

        self.assertEqual(obj.deposit([0, 0, 2, 1, 1]), "void")
        self.assertEqual(obj.withdraw(700), [0, 0, 0, 1, 1])

    def test_withdraw_zero(self):
        obj = ATM()
        self.assertEqual(obj.withdraw(0), "Error: Amount must be between 1 and 10^9")

    def test_deposit_invalid_input_length(self):
        obj = ATM()
        self.assertEqual(obj.deposit([0, 0, 1, 2]), "Error: banknotesCount.length must be 5")

    def test_deposit_invalid_input_value(self):
        obj = ATM()
        self.assertEqual(obj.deposit([0, 0, 1, 2, -1]), "Error: Each banknote count must be between 0 and 10^9")

    def test_withdraw_insufficient_funds(self):
        obj = ATM()
        self.assertEqual(obj.deposit([1, 1, 1, 1, 1]), "void")
        self.assertEqual(obj.withdraw(1000), [-1])


if __name__ == '__main__':
    unittest.main()