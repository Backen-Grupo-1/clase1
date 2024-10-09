# Ejercicio 1
# • Elaborar el código para el cálculo de la raíz cuadrada de un número.
# • Restricción: no se puede usar sqrt de la biblioteca de Python.
# • Debe solicitar el número por la entrada estándar e imprimir el resultado.

numero_entrada = int(input("Ingrese un número: "))
if numero_entrada <= 0:
    print("No se puede calcular la raíz cuadrada de un número negativo.")
else: 
    raiz_cuadrada = numero_entrada ** 0.5
    print(f"la raiz cuadrada de {numero_entrada} es: {raiz_cuadrada}.")

# Ejercicio 2
# Elaborar un código para el cálculo de la distancia euclidiana entre dos puntos.
# • Recuerde que la distancia euclidiana se calcula en base a las coordenadas x e y
# de ambos puntos.
# • Debe solicitar las coordenadas de los puntos por la entrada estándar e imprimir la
# distancia.
# • La fórmula del cálculo es:

x1 = int(input("Ingrese la primera coordenada: "))
y1 = int(input("Ingrese la segunda coordenada: "))
x2 = int(input("Ingrese la tercera coordenada: "))
y2 = int(input("Ingrese la cuarta coordenada: "))

# distancia_euclidiana = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print(f"La distancia euclidiana es: {distancia_euclidiana}.")

# Ejercicio 3
# Escriba un programa que solicite al usuario una palabra.
# • Invierta la palabra y guárdela en una nueva variable.
# • Imprima por pantalla la palabra original y luego la palabra invertida

palabra = input("Ingrese una palabra: ")
palabra_invertida = palabra[::-1]
print(f"La palabra original es: {palabra}, la palabra invertida es: {palabra_invertida}.")