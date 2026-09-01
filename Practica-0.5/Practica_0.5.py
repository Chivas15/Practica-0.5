aves = ["Gallina", "Cuervo", "Aguila"] #lista ya establecida con aves.

print("Lista de aves: ") #impresion de la lista inicial
for i in range(len(aves)):
    print(i, ":", aves[i])

#se agrega la nueva ave 
nueva_ave = input("Escribe el nombre del ave que quieres agregar al final: ")
aves.append(nueva_ave) #la funcion .append es para agregar un unico elemento al final de una lista, en este caso aves

print("\nlista de aves: ") #impresion de la lista
for i in range(len(aves)): #el len es para ver los elementos de la lista, lo pasa aqui es que el for asigna a i 
    #a tomar todas las variables que hay en la lista aves, el print imprime el valor de i que son las posiciones de la lista
    # y depues va a aves[i] para sacar sus elementos
    print(i, ":", aves[i]) 
