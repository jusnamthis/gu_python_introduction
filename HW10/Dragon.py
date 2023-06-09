import math


class Dragon:
    def __init__(self, height, dangerous, color):
        self.height = height
        self.dangerous = dangerous
        self.color = color


    def __add__(self, d2):
        new_color = d2.color if self.color > d2.color else self.color
        new_height = math.floor((self.height + d2.height)/2)
        new_dangerous = self.dangerous if self.dangerous > d2.dangerous else d2.dangerous
        return Dragon(new_height, new_dangerous, new_color)


    def __lt__(self, other):
        if self.height < other.height:
            return True
        if self.dangerous < other.dangerous:
            return True
        if self.color < other.color:
            return True
        return False


    def __le__(self, other):
        if self.height <= other.height:
            return True
        if self.dangerous <= other.dangerous:
            return True
        if self.color <= other.color:
            return True
        return False


    def __eq__(self, other):
        if self.height == other.height:
            return True
        if self.dangerous == other.dangerous:
            return True
        if self.color == other.color:
            return True
        return False


    def __ne__(self, other):
        if self.height != other.height:
            return True
        if self.dangerous != other.dangerous:
            return True
        if self.color != other.color:
            return True
        return False


    def __gt__(self, other):
        if self.height > other.height:
            return True
        if self.dangerous > other.dangerous:
            return True
        if self.color > other.color:
            return True
        return False


    def __ge__(self, other):
        if self.height >= other.height:
            return True
        if self.dangerous >= other.dangerous:
            return True
        if self.color > other.color:
            return True
        return False
    

    def __isub__(self, number):
        self.height -= self.height // number
        self.dangerous += self.dangerous % number
        return self
    

    def __call__(self, str):
        return self.dangerous * str
    

    def change_color(self, new_color):
        self.color = new_color


    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.dangerous} and {self.color} color.'
    

    def __repr__(self):
        return f'{self.__class__.__name__}({self.height}, {self.dangerous}, {self.color})'



