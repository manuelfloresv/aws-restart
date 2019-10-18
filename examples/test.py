wordids={"a":1 , "b":2,"c":3,"d":4,"e":5,"f":6,"g":7}

a = []
print(wordids)
#for wi,val in wordids.items():
for wi in wordids:    
  a.append(str(wordids[wi]))
print(a)

c = [str(wi.upper()) for wi in wordids]
print(c)


counter=0
while counter <= 3:
  print("I love learning lython!!")
  counter=counter+1

  # Python program to print 
# colored text and background 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 
  
prCyan("Hello World, ") 
prYellow("It's") 
prGreen("Geeks") 
prRed("For") 
prGreen("Geeks") 