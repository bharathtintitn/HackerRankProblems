import sys


class Nool(int):

    def __new__(cls, val=0):
        if val:
            return true
        else:
            return false

    def __repr__(self):
        if self:
            return true
        else:
            return false

    __str__ = __repr__







if __name__ == "__main__":

    false = int.__new__(Nool,0)
    print false
    true = int.__new__(Nool,1)
    print true
