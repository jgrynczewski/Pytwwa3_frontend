# lambda, filter, map, reduce ...
# Funkcje - First class citizen
# Funkcje wyższego rzędu (higher-order function)

def f(x):
    return x**2

print(f(2))

g = lambda x: x**2
print(g(2))

# map - pozbywamy się pętli
a_list = [1,2,3,4]

new_list = []
for i in a_list:
    new_list.append(i**2)

new_list = map(f, a_list)

# filter - pozbywamy się warunków

def h(x):
    if x%2 == 0:
        return True
    return False

new_list = filter(h, a_list)

# Funkcje anonimowe
new_list = map(lambda x: x**2, a_list)
new_list = filter(lambda x: x%2==0, a_list)

# Znajdźmy kwadrat liczb naturalnych od 1 do 10 o wartościach
# większych niż 50

new_list = []
for item in range(1, 11):
    if (item**2 > 50):
        new_list.append(item**2)
print(new_list)

# Paradygmat funkcyjny
print(list(filter(lambda x: x>50, map(lambda x: x**2, range(1, 11)))))