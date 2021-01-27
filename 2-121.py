def vertice(a, b, c):
    delta = b**2-4*a*c
    vertice = (-b/(2*a))*(-delta/(4*a))
    print(vertice)

def fuoco(a, b, c):
    delta = b**2-4*a*c
    fuoco = (-b/(2*a))*(1-delta)/(4*a)
    print(fuoco)

a = int(input("valore di a = "))
b = int(input("valore di b = "))
c = int(input("valore di c = "))
vertice(a, b, c)
fuoco(a, b, c)

