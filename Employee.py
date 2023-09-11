class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getID(self):
        return self.__employee_id
    
    def toString(self):
        return "ID: " + str(self.getID()) + ", Nome: " + self.getName() + ", Salário: R$" + str("{:.2f}".format(self.getSalary()))
    
    def setSalary(self, salary):
        self.__salary = salary

    def setName(self, name):
        self.__name = name

    def setID(self, employee_id):
        self.__employee_id = employee_id
        
    