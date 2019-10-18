# python3.6  
# coding: utf-8  
# store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
#Counts how many y are in insuling string
print(float(insulin.count("y")) )

#Will count how many letter has insulin in their string
#Output example: {'y': 4.0, 'c': 6.0, 'k': 1.0, 'h': 2.0, 'r': 1.0, 'd': 0.0, 'e': 4.0}
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)

pH=0

#Caculate the value ph the pH valur of each letter
#Output example:{'k': 0.9999999999704879, 'h': 1.999998000002, 'r': 0.9999999999996688}
print({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x])))   for x in ['k','h','r']})
#Summ all the values 
#Output example: 3.9999979999721567
print(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x])))   for x in ['k','h','r']}.values()))
print("pp")


#Calculate the netCharge substracting ycde sequence from khr sequence
#Output example: 3.999773036108418
netCharge = (   +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
print(netCharge)

while (pH <= 14):
  netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
  print('{0:.2f}'.format(pH), netCharge)
  pH=pH+1
