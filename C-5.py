"""
3歳以下の入場料金は無料にしてください
"""
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        # こうかな？？
        if self.age <= 3:
            fee = 0
        elif 4 < self.age < 20:
            fee = 1000
        elif 20 <= self.age < 65:
            fee = 1500
        else:
            fee = 1200

        return fee

    def info_csv(self):
        new_list = [self.first_name + ' ' + self.family_name, self.age, self.entry_fee()]

        return new_list


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_csv())
tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_csv())
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())
# ちょっと違うかも！！！
