import random
import math

print("Zad1")
print("A")
A = [1 - x for x in range(0, 11)]
print(A)
print("B")
B = [4 ** x for x in range(0, 8)]
print(B)
print("C")
C = [x for x in B if x % 2 == 0]
print(C)


print("Zad2")
list = []
for i in range(1, 11):
    list.append(int(random.random() * 100))
list1 = [x for x in list if x % 2 == 0]
print(list1)


print("Zad3")
sklep = {"Bułka": "szt", "Pomidor": "kg", "Wędlina": "kg", "Chleb": "szt"}
sklepszt = {k: v for k, v in sklep.items() if v == "szt"}
print(sklepszt)


print("Zad4")
def trojkat(a, b, c):
    if a > b and a > c:
        if a ** 2 == b ** 2 + c ** 2:
            return "Trójkąt jest prostokątny"
        else:
            return "Trójkąt nie jest prostokątny"
    elif b > a and b > c:
        if b ** 2 == a ** 2 + c ** 2:
            return "Trójkąt jest prostokątny"
        else:
            return "Trójkąt nie jest prostokątny"
    if c > b and c > a:
        if c ** 2 == b ** 2 + a ** 2:
            return "Trójkąt jest prostokątny"
        else:
            return "Trójkąt nie jest prostokątny"
print(trojkat(3, 4, 5))


print("Zad 5")
def trapez(a=5, b=6, h=10):
    pole = ((a + b) * h) / 2
    return pole

print(trapez())


print("Zad 6")
def ciag(a=1, b=4, ile=10):
    iloczyn = 1
    for i in range(ile):
        iloczyn *= a * b ** i
    return iloczyn
print(ciag())


print("Zad 7")
try:
    liczba = int(input("Podaj liczbę do spierwiastkowania: "))
    result = math.sqrt(liczba)
except Exception:
    print("Error")
else:
    print(result)
