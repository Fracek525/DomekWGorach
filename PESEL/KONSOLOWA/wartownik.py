import random

def tablica():
    tab = [random.randint(0,5) for _ in range(50)]
    return tab


def wartownik(tab,a):
    print(tab)
    tab.append(a)
    for i in range(len(tab)-1):
        if (tab[i] == a):
            return i
    raise Exception()

try:
    i = wartownik(tablica(), int(input("Jakiej liczby szukasz: ")))
    print(i)
except:
    print("Nie znaleziono liczby.")

