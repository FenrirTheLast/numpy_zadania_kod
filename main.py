import numpy as np
# zad1
a = np.arange(3, 3*15+1, 3)
print(a)


# zad2
lista = [1.5, 2.3, 4.7, 3.6, 6,7]
a = np.array(lista)
print(a)
b = a.astype(dtype='int64')
print(b)
c = np.array(lista, dtype='int32')
print(b)

# zad3
def tablica(n):
    a = np.zeros((n*n), dtype='int32')
    for i in range(0, len(a)):
        a[i] = i+1
    tab = a.reshape((n, n))
    # b = np.arange(1, 26, 1).reshape((n, n))
    return tab
#
print(tablica(5))

# zad4
def generuj(liczba, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=liczba)

print(generuj(2,4))

# zad5
def diagonalna(n):
    a = np.arange(n, 0, -1)
    diag = np.diag(a)
    return diag

print(diagonalna(4))

# zad6
malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
armata = np.flip(armata)

wykreslanka = np.zeros((6,6), dtype='str')

print(wykreslanka)

wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = malina
#wykreslanka[5,::-1] = armata
wykreslanka[5,:] = armata
print(wykreslanka)
print("")
wykreslanka[:, 0] = mrowka
wykreslanka[5,::-1] = armata
for a in range(5):
    wykreslanka[a,a] = malina[a]
print(wykreslanka)

# zad7
def macierz(n):
    mac = np.zeros((n, n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2*(2*i) for _ in range(n-i)], k=i)
        mac += np.diag([2*(2*i) for _ in range(n-i)], k=-i)
    print(mac)
#
macierz(5)

# zad8
def podziel(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę kolumn")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)


podziel(np.arange(49).reshape((7, 7)), kierunek='pionowo')

# zad9
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


macierz = np.ones(25, dtype='int32')
print(macierz)
for a in range(0, 25, 1):
    element = fib(a)
    macierz[a] = element

macierz = macierz.reshape((5, 5))
print(macierz)