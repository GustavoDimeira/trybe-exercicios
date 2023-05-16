class Math:
  def __init__(self) -> None:
    pass
  
  def media(self, numbers):
    total = 0
    for number in numbers:
      total += number
    return total / len(numbers)

  def mediana(self, numbers):
    numbers.sort()
    middle = len(numbers) / 2
    if (len(numbers) % 2 == 0):
      return (numbers[int(middle - 0.5)] + numbers[int(middle + 0.5)]) / 2
    return numbers[int(middle)]

  def moda(self, numbers):
    repetitions = {}
    for number in numbers:
      key = str(number)
      if key in repetitions.keys():
        repetitions[key] += 1
      else:
        repetitions[key] = 1

    return repetitions
