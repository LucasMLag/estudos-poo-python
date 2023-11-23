from person import Person

john1 = Person('John', 'Doe', True, ['R1'])
john2 = Person('John', 'Doe', True, ['R2'])
mary = Person('Mary', 'Jane', False, ['R3'])
print(john1)
print(john1.addresses)
print(john1.fullname)
print(john1 == john2)
print()
