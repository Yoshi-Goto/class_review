"""
単一顧客の情報取得をタブ区切りにも対応させてください
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
        elif 3 < self.age < 20:
            fee = 1000
        elif 20 <= self.age < 65:
            fee = 1500
        elif 65 <= self.age < 75:
            fee = 1200
        else:   # こんな感じ？？
            fee = 500

        return fee

    def info_tab(self):
        ret = self.first_name + ' ' + self.family_name + '\t' + str(self.age) + '\t' + str(self.entry_fee())

        return ret


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_tab())
tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_tab())
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_tab())
# ちょっと違うかも！！！
