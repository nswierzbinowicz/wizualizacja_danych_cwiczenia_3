import math
# try:
#     a = int(input())
#     b = int(input())
#     result = a / b
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("wrong value")
# except Exception:
#     print("Error")
# else:
#     print(result)

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = []
# for i in list1:
#     list2.append(pow(i,2))
# print(list2)
# list2 = [x**2 for x in list1]
# print(list2)
# list3 = [3**y for y in range(0,6)]
# print(list3)
# list4 = [x for x in list2 if x%2==1]
# print(list4)
# list5 =  [(x,y) for x in list3 for y in list4]
# print(list5)

# slownik1 = {1 : 2 , 2 : 3 , 3 : 4, 4 : 5}
# slownik2 = {}
# for key, value in slownik1.items():
#     slownik2[value] = key
# print(slownik1)
# print(slownik2)
# slownik3 = {v : k for k, v in slownik1.items()}
# print(slownik3)

# def rownanie_kwadratowe(a,b,c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print("Brak pierwiastków")
#         return 0
#     elif delta == 0:
#         print("Jeden pierwiastek")
#         x = (-b) / 2 * a
#         return x
#     elif delta > 0:
#         print('Dwa pierwiastki')
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         return x1,x2
# print(rownanie_kwadratowe(1,2,1))
# print(rownanie_kwadratowe(6,1,3))
# print(rownanie_kwadratowe(1,4,2))

# def dlugosc_odcinka(x1=1,x2=2,y1=3,y2=4):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(4,2,6,3))
# print(dlugosc_odcinka(y2=5,y1=5,x2=2,x1=8))
# plik = open('tekst.txt','r', encoding='utf-8')
# znaki = plik.read(10)
#
# linia = plik.readline()
# linie = plik.readlines()
# plik.close()
# print(linia)
# print(linie)
# for l in linie:
#     print(l)
# plik = open('zapis.txt','a+')
# plik.write('siala baba mak nie wiedziala jak')
# plik.seek(105)
# znaki = plik.read()
# plik.close()

with open('tekst.txt','r') as f:
    lines = f.readlines()

print(lines)