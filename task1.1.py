class Number:
    def __init__(self,x: int):
        self.number = x

    def check(self, num1: int, num2: int, num3: int) -> bool:
        return self.number == num1 + num2 + num3
