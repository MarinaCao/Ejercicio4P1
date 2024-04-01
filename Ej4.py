# Definimos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iteramos sobre cada número en la lista
for numero in numeros:
    # Verificamos si el número es impar
    if numero % 2 != 0:
        # Si es impar, continuamos con la siguiente iteración sin imprimirlo
        continue
    # Si el número es par, lo imprimimos
    print(numero)
