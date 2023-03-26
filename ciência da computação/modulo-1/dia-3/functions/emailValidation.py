notValid = True

def hasError():
  print("invalid email type")
  print("  *-----*  \n\n\n")
  username, domain, extention = "", "", ""

while (notValid):
  print("*-----*-----*")
  print("Insert a valid email: ")
  email = input()

  try:
    splited = email.split("@")
    username = splited[0]
    domain, extention = splited[1].split(".")

    if(not username[0].isalpha() or not username.isalnum() or not domain.isalnum() or len(extention) > 3):
      raise ValueError("invalid format")

    notValid = False    
  except IndexError:
    hasError()
  except NameError:
    hasError()
  except ValueError:
    hasError()

print(username, domain, extention)
