"""
次のコードが正しく動作するような Square クラスを実装してください
diagonal は 対角線(の長さ) という意味です。
"""

import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        ret = self.side * self.side

        return ret

    def diagonal(self):
        ret = math.sqrt(pow(self.side, 2) + pow(self.side, 2))

        return ret


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
