class ContagemIterable:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        
        else: 
            raise StopIteration



valor_maximo = int(input("Digite o valor máximo: "))

num = ContagemIterable(valor_maximo)

i = iter(num)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))