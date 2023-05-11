"""
Crie um algoritmo não recursivo para contar quantos números pares existem em uma sequência numérica (1 a n).
"""

def count_odd(n): return ValueError("N deve ser maior que 0") if (n < 0) else int(n/2)


print(count_odd(-11))
