class Customer:
    def __init__(self, first_name, family_name):
        self.full_name = first_name + ' ' + family_name


Ken = Customer(first_name='Ken', family_name='Ford')
print(Ken.full_name)
