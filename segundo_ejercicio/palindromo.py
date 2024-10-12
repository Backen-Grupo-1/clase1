"""
¿Es palíndromo?
• Escriba un programa reciba como entrada una palabra.
• Determine si la palabra ingresada es palíndroma.
• Imprima por pantalla si la palabra es palíndroma.
"""

def palindromo(palabra):
    if palabra == palabra[::-1]:
        print(f"La palabra {palabra} es palindrome")
    else:
        print(f"La palabra {palabra} no es palindrome")

palabra = input("Ingrese una palabra: ")
palindromo(palabra)
