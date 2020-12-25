
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))


class Number:
    def __init__(self, x: int):
        self.number = x
        s = Number(a+b+c)

    def check(self, num1: int, num2: int, num3: int) -> bool:
        return self.number == num1 + num2 + num3


print(s.check())
