palabra = input("ingrese una palabra o frase: ")
palabra.lower()
ok = True
indi = 0
lista_nueva = []
for elem in palabra:
    lista_nueva.append(elem)
# primero pasamos el string a una lista 
print(lista_nueva)
while ok and indi < len(palabra):
    car = lista_nueva[indi]
    if car.isalpha() and lista_nueva.count(car) != 1:
        ok=False
        print("el caracter repetido es: ", car)
    indi += 1
#recorremos la lista mientras que sea verdad que no se repite el caracter en la frase
print("la palabra ES Herterograma " if ok else " la palabra NO era Heterograma" )