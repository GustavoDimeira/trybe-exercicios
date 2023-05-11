"""
Transforme o algoritmo criado acima em recursivo.
"""

def count_odd(n, counter = 0):
  if (n < 1): return counter
  else:
    if (n % 2 == 0): return count_odd(n - 1, counter + 1)
    else: return count_odd(n - 1, counter)

print(count_odd(5))
print(count_odd(8))
print(count_odd(25))
print(count_odd(0))