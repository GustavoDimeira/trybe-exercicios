import json
import csv

boockCategoryRelation = {}

def getPercentageByCategory():
  with open('books.txt', 'r') as books:
    totalBoocks = 0
    content = json.loads(books.read())
    for boock in content:
      for category in boock["categories"]:
        if(boockCategoryRelation.get(category)):
          boockCategoryRelation[category] += 1
          totalBoocks += 1
        else:
          boockCategoryRelation[category] = 1
          totalBoocks += 1
    for categoryAmount in boockCategoryRelation.keys():
      boockCategoryRelation[categoryAmount] = (boockCategoryRelation[categoryAmount] * 100) / totalBoocks

  with open("categoryPercentage.csv", "w", encoding = "utf-8") as file:
    writer = csv.writer(file)

    headers = [
        "categoria",
        "porcentagem",
    ]
    writer.writerow(headers)

    for categoria, porcentagem in boockCategoryRelation.items():
      row = [
          categoria,
          porcentagem,
      ]
      writer.writerow(row)

getPercentageByCategory()
