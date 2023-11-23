class Person:
    def __init__(self, firstname, lastname):
        self.name = firstname
        self.lastname = lastname

    def __str__(self):
        class_str = f'{self.__class__.__name__}' f'({self.name} {self.lastname})'
        return class_str
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, o):
        return self.lastname == o.lastname
