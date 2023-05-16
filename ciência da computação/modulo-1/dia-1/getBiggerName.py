def getBiggerName(names):
  biggerName = ''
  for name in names:
    if len(name) > len(biggerName):
      biggerName = name
  return biggerName