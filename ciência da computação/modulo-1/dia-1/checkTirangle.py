def verifyTriangle(s1, s2, s3):
  if (s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
    if (s1 == s2 and s2 == s3):
      return "Triangulo equilatero"
    if (s1 == s2 or s1 == s3 or s2 == s3):
      return "Triangulo isosceles"
    return "Triangulo escaleno"
  return "Não é um triangulo"