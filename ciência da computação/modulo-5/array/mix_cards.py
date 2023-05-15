import random


"""
Exemplo 1:
cartas = [2, 6, 4, 5]
cartas por parte = 2

resultado = [2, 4, 6, 5]

Exemplo 2:
cartas = [1, 4, 4, 7, 6, 6]
cartas por parte = 3

resultado = [1, 7, 4, 6, 4, 6]
"""


def mix_cards(cards):
    middle_index = len(cards) // 2
    list1, list2 = cards[:middle_index], cards[middle_index:]

    positions = []

    while (len(positions) < len(cards)):
        number = int(random.random() * len(cards))
        if (not number in positions):
            positions.append(number)

    mixed_cards = []

    for index in positions:
        if (index < middle_index):
            mixed_cards.append(list1[index])
        else:
            mixed_cards.append(list2[index - middle_index])

    return mixed_cards
