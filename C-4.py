"""
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
"""


class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        if self.age < 20:
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
