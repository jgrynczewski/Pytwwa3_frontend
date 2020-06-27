# Przekazywanie przez wartość (kopiowanie wartość)
a = 5

def func(a):
    a += 1
    return a

func(a)
print(a)

# Przekazywanie przez referecję (kopiowanie adresu)
# Wszystkie typy złożone + klasy i obiekty
b = [1, 2, 3]

def func2(x):
    x.append(4)

func2(b)
print(b)

class MojKlasa():
    def __init__(self, a_list):
        self.a_list = a_list

    def rozszerz(self):
        self.a_list.extend([10,20])

m = MojKlasa(b)
m.rozszerz()

print(b)