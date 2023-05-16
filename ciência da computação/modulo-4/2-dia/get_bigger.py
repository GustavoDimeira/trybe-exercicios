"""
Crie um algoritmo recursivo que encontre, em uma lista, o maior número inteiro
"""

a = [1, 5, 13, 3, 9, 15, 2, 0, -15, 25]


def get_bigger(list_numbers, position=0, bigger=False):
    if (position == 0): bigger = list_numbers[position]
    if (position < len(list_numbers)):
        if (list_numbers[position] > bigger):
            bigger = list_numbers[position]

        bigger = get_bigger(list_numbers, position + 1, bigger)

    return bigger


print(get_bigger(a))
