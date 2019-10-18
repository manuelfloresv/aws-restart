import random 

def mattEducation():
 options=["Failure","Success"]
 return random.choices(options)[0]

noobs=mattEducation()

if noobs == "Success":
  print("Tons of money")
else:
  print("Get good")
