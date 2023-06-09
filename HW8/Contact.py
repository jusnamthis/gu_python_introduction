class Contact:
    def __init__(self, phoneNumber, name, lastname=" ", middlename=" ", birthdate=" "):
        self.name = name
        self.lastname = lastname
        self.middlename = middlename
        self.birthdate = birthdate
        self.phoneNumber = phoneNumber


    def get_str_repr_delim(self):
        return '--'


    def __repr__(self):
        delim = self.get_str_repr_delim()
        return f'{self.phoneNumber}{delim}{self.name}{delim}{self.lastname}{delim}{self.middlename}{delim}{self.birthdate}'

    
    def __str__(self):
        return f'\n{self.phoneNumber}\n{self.name}\n{self.middlename}\n{self.lastname}\n{self.birthdate}\n'
