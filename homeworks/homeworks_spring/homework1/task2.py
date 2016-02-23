__author__ = 'Independence'


class fibonacci_sequence:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 0:
            self.i += 1
        if self.i == 1 and self.i <= self.n:
            self.i += 1
            return 1
        elif self.i <= self.n:
            value = self.a + self.b
            self.a = self.b
            self.b = value
            self.i += 1
            return value
        else:
            raise StopIteration("Finished")
