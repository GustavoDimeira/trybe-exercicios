"""
Escreva um algoritmo recursivo para encontrar o máximo divisor comum (mdc) de dois inteiros.
"""

def get_mdc(num1: int, num2: int, counter = 1, mdc = 1):
    if (counter <= num1 and counter <= num2):
        if (num1 % counter == 0 and num2 % counter == 0):
            mdc = counter
        return get_mdc(num1, num2, counter + 1, mdc)
    return mdc


print(get_mdc(4.2, 64))
