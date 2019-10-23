#!/sbin/python

employeesNames=["Matt","Paul","Jackie","Tommy","Jaheeimm","Neil"]
class Employees:
    employees =[]
    def setEmp(self,employees):
       return {'employees': [i[0] for i in employees]} # Fetches first column that is Employee ID

#class Employees:
#    __employees = ''     #protected


#    def __init__(self,details={}):  # constructor
#        self.employees = details
#    def set_emp(self,details):        # function
#        self.__employees = details

#    def get_emp(self):
#        return self.__employees
#
#    def set_pp(self,details):        # function
#        self.__employees = details
#        return self.__employees
#        return details


#vvar =  Employees()
#vvar.set_emp(employeesNames)
#print(vvar.get_emp())
#print(vvar.set_pp(employeesNames))


vvar =  Employees()
#vvar.set_emp(employeesNames)
#print(vvar.get_emp())
print(vvar.setEmp(employeesNames))
