code = [
  ("0"),
  ("1"),
  ("A", "B", "C"),
  ("D", "E", "F"),
  ("G", "H", "I"),
  ("J", "K", "L"),
  ("M", "N", "O"),
  ("P", "Q", "R"),
  ("S", "T", "U", "V"),
  ("W", "X", "Y", "Z"),
]

print('insert the phone number')
numberEncoded = input()
response = ""

for letter in numberEncoded:
  elementLenth = len(response) + 0
  if (letter == "-"):
    response += letter
  else:
    for i, element in enumerate(code):
      if (letter in element):
        response += str(i)
    if (elementLenth == len(response)):
      print("invalid caravtery")

print(response)
