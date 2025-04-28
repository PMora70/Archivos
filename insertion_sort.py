def insertion_sort(lista):
    
    for i in range(1, len(lista)):
        
        clave = lista[i]
       
        j = i - 1
       
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = clave
    
    return lista

lista = [12, 11, 13, 5, 6]
print("Lista original:", lista)
lista_ordenada = insertion_sort(lista)
print("Lista ordenada:", lista_ordenada)
