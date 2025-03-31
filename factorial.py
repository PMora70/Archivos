num = int(input("Ingrese un numero: "))
if num < 0:
    print("No existe factorial de un negativo.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *=i 
print(f"El factorial de {num} es {factorial}")
                