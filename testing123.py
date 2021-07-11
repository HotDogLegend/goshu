class Test:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get(self, val: int) -> int:
        if val=='a':
            return self.a
        elif val=='b':
            return self.b
        elif val=='c':
            return self.c
        else:
            return 0

    def set(self, item: str, val: int) -> None:
        if item=='a':
            self.a = val
        elif item=='b':
            self.b = val
        elif item=='c':
            self.c = val
        


n = Test(4, 2, 5)

print(n.get('a'))
n.set('a', 20)
print(n.get('a'))