response = []

print('What is the maximun number?\n')
max = input()

for n in range(int(max)):
  if (not (n + 1) % 3): response.append('fizz')
  elif (not (n + 1) % 5): response.append('buzz')
  else: response.append(n + 1)

print(response)