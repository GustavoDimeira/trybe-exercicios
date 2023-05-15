"""
entradas = [1, 2, 3]
saidas = [3, 2, 7]
instante_buscado = 4
resultado: 1

O estudante 1 entrou no instante 1 e saiu no 3, já o segundo entrou
e saiu no 2 e o último foi único a estar presente no instante 4.
"""

def count_people_in(in_times, out_times, target_time):
    in_before_target = 0

    for time in in_times:
        if (time < target_time): in_before_target += 1

    for time in out_times:
        if (time < target_time): in_before_target -= 1

    return in_before_target
