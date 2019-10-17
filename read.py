import re
pattern = "[a-z]+" #Regular expresion
f = open('preproinsulin_seq.txt', 'r')
pSequence="" #Protein Sequence

#Function to save a line in a file (Replace content in the file)
def saveFile(fileName,saveString):
  #Save saString into file fileName
  f = open(fileName, "w")
  f.write(saveString+"\n")
  f.close()
  return 0

#From https://www.ncbi.nlm.nih.gov/protein/AAA59172.1 | File format : 
#ORIGIN      
#    1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
#   61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
#//


#Find the pattern in the sequence file. 
for i, line in enumerate(f):
  #print(i)
  #print(pSequence)

  #Find the pattern and write and save it into a string
  find = re.findall(pattern,line)
  #print(find)
  for element in find:
    pSequence=pSequence+element
    #print(pSequence)
  
print("Insulin protein sequence is:"+pSequence)
f.close()


if len(pSequence) == 110:
  #Save de 110 char string found
  #Open the file in writing mode and save results manualy
  f = open("preproinsulin_seq_clean.txt", "w")
  f.write(pSequence+"\n")
  f.close()
  
  insulin=pSequence[0:24]
  print("Insulin-->>"+insulin+":"+str(len(insulin)))
  #Savinf the file throug a function
  saveFile("Iinsulin_seq_clean.txt",insulin)

  binsulin=pSequence[24:54]
  print("Binsulin-->>"+binsulin+":"+str(len(binsulin)))
  saveFile("binsulin_seq_clean.txt",binsulin)

  cinsulin=pSequence[54:89]
  print("Cinsulin-->>"+cinsulin+":"+str(len(cinsulin)))
  saveFile("cinsulin_seq_clean.txt",cinsulin)
  
  ainsulin=pSequence[89:110]
  print("Ainsulin-->>"+ainsulin+":"+str(len(ainsulin)))
  saveFile("ainsulin_seq_clean.txt",ainsulin)
else:
  print("FAIL: Sequence is not 110 character")