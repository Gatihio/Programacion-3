"""
Primer Ejercicio semanal
"""

class Solution:
    """
    Clase que contiene el método para eliminar elementos de una lista.
    """
    def remove_element(self, nums, val):
        """
        Elimina todas las ocurrencias de val en nums in-place y retorna
        la cantidad de elementos diferentes a val.
        """
        k = 0
        for _, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1

        return k
    