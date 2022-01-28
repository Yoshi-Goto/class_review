"""
料金の計算ルール
こども料金(20歳未満): 1000円
おとな料金(20歳以上65歳未満): 1500円
シニア料金(65歳以上): 1200円
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.entry_fee() # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee() # 1200 という値を返す
"""
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        fee = 0
        if self.age < 20:
            fee = 1000
        elif 20 <= self.age < 65:
            fee = 1500
        else:
            fee = 1200

        return fee


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())
tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.entry_fee())  # 57 という値を返す
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee())  # 73 という値を返す
