"""
Este módulo contiene una función para encontrar todas las combinaciones
de tres números en una lista que suman cero.
"""

def tres_sumas(numeros):
    """
    Encuentra todos los tripletes únicos en la lista que suman cero.
    
    :param numeros: Lista de números enteros.
    :return: Lista con los tripletes que suman cero.
    """
    numeros.sort()
    resultado = []

    for i in range(len(numeros)):
        if i > 0 and numeros[i] == numeros[i - 1]:
            continue

        izquierda = i + 1
        derecha = len(numeros) - 1

        while izquierda < derecha:
            suma = numeros[i] + numeros[izquierda] + numeros[derecha]

            if suma == 0:
                resultado.append([numeros[i], numeros[izquierda], numeros[derecha]])

                while izquierda < derecha and numeros[izquierda] == numeros[izquierda + 1]:
                    izquierda += 1
                while izquierda < derecha and numeros[derecha] == numeros[derecha - 1]:
                    derecha -= 1

                izquierda += 1
                derecha -= 1

            elif suma < 0:
                izquierda += 1
            else:
                derecha -= 1

    return resultado


# Prueba del código
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    tripletes = tres_sumas(nums)
    print("Tripletes que suman cero:", tripletes)
