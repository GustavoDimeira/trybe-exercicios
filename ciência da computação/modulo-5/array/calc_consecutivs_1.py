"""
1 - OK
0 - Instabilidades

valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]
resultado = 3

valores_coletados = [1, 1, 1, 1, 0, 0, 1, 1]
resultado = 4
"""

def count_consecutive_hours(list_checks):
    list_checks.append(0)
    crr_max, new_sequence = (0, 0)
    for check in list_checks:
        if (check):
            new_sequence += 1
        else:
            if (crr_max < new_sequence):
                crr_max = new_sequence
            new_sequence = 0
    return crr_max
