# import pprint
from pprint import pprint
#import importme
from importme  import helloall

def output(mode, var, element):
  if mode == "simple":
    pprint(var.upper())
    return 0
  elif mode == "dict":
    pprint(var.get(element))
    return 0
  elif mode == "list":
    pprint(var)
    return 0
  else:
    return 1
    
#importme.helloall()
helloall()

classes = [ 
  "history", "animation", "art", "math", 
  "english", "philosophy", "science", "homeecon", 
  "pe", "compsci" 
]

# print("Print 'classes'")
# print(classes[4])
# print(classes[5])
# print(classes[6])

# # print(classes[4:])
# classes2019 = classes[4:]
# classes2019.append("spanish")
# print(classes2019)

output("simple", "Working on Dictionaries", None)

students = [ { "grade": 5, "firstname": "Joseph", "lastname": "Barn", "gender": "M" },
  { 
    "grade": 7,
    "firstname": "Freddy",
    "lastname": "Mercury",
    "gender": "M" 
  },
  { 
    "grade": 12,
    "firstname": "Cher",
    "lastname": "Starbucks",
    "gender": "F" 
  }
]

output("list", students, None)

classes2019 = [ 
  {
    "classname": "history",
    "classid": 16,
    "classlevel": 101,
    "teacher": "Bob",
    "classroom": "66B",
    "grades": [ 5, 6, 7 ]
  },
  {
    "classname": "history",
    "classid": 17,
    "classlevel": 201,
    "teacher": "Bob",
    "classroom": "66D",
    "grades": [ 8, 9 ]
  },
  {
    "classname": "math",
    "classid": 2,
    "classlevel": 101,
    "teacher": "Martha",
    "classroom": "12A",
    "grades": [ 5, 6 ]
  },
  {
    "classname": "math",
    "classid": 4,
    "classlevel": 201,
    "teacher": "Martha",
    "classroom": "12C",
    "grades": [ 7 ]
  },
  {
    "classname": "philosophy",
    "classid": 18,
    "classlevel": 101,
    "teacher": "Bartholemew",
    "classroom": "00Z",
    "grades": [ 9 ]
  },
  {
    "classname": "getajob",
    "classid": 82,
    "classlevel": 10000,
    "teacher": "Jo Momma",
    "classroom": "42A",
    "grades": [ 12 ]
  },
 ]

output("list", classes2019, None)

for c in classes2019:
  if c.get('classname') == "getajob":
    # pprint(c.get('classname'))
    output("dict", c, 'classname')
    # pprint(c.get('grades'))
    output("dict", c, 'grades')
  elif c.get('classname') == "math" and c.get('classlevel') == 101:
    # pprint(c.get('classname'))
    output("dict", c, 'classname')
    # pprint(c.get('classlevel'))
    output("dict", c, 'classlevel')
  else:
    # pprint("no matches here")
    output("simple", "No Matches Here", None)
    # pprint(c.get('classname'))
    output("dict", c, 'classname')



response = output("simple", "Testing an Error", None)
# print(response)
if response != 0:
  print("Danger Will Robinson!")


# classes2019 = list(set(classes))
# print("Print 'classes2019'")
# print(classes2019)

# # classes.append("compsci")

# classes2020 = classes

# print("Print 'classes2019'")
# print(classes2019)
# print("Print 'classes2020'")
# print(classes2020)