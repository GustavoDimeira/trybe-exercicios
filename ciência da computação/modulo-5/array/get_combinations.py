"""
Exemplo 1:
produtos = [1, 3, 1, 1, 2, 3]
resultado = 4
Os índices (0, 2), (0, 3), (1, 5), (2, 3) formam combinações.

Exemplo 2:
produtos = [1, 1, 2, 3]
resultado = 1
Os índices (0, 1) formam a única combinação.
"""


def get_combinations(list):
    combs = []
    for crr_iten_index in range(len(list)):
        for to_compare_index in range(crr_iten_index + 1, len(list)):
            if (list[crr_iten_index] == list[to_compare_index]):
              combs.append((crr_iten_index, to_compare_index))
    return combs, len(combs)
