def printName(name):
  fullname = ''
  nameIncreasingList= []
  for letter in name:
    fullname += letter
    nameIncreasingList.append(fullname)

  nameIncreasingList.reverse()
  print(nameIncreasingList)

printName('name')
