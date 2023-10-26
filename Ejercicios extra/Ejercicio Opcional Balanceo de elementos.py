def validar_parentesis(expresion):
    pila = []
    # Mapeo de paréntesis
    parejas = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in "([{":
            # Si es un paréntesis de apertura, agrégalo a la pila.
            pila.append(caracter)
        elif caracter in ")]}":
            # Si es un paréntesis de cierre, verifica si coincide con el tope de la pila.
            if not pila or pila[-1] != parejas[caracter]:
                return False
            pila.pop()

    # Al final, la pila debe estar vacía si todos los paréntesis están balanceados.
    return len(pila) == 0

# Ejemplo de uso:
expresion = "((3 + 2) * [5 - 1])"
if validar_parentesis(expresion):
    print("Los paréntesis están balanceados correctamente.")
else:
    print("Los paréntesis no están balanceados correctamente.")

# El ejemplo funciona bien para todos los casos, se puede probar colocando incluso {} para verificar que igual es correcto o quitar alguno para ver que da error