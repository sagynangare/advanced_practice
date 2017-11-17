#How to create attribute of a class without passing and instantiating in constructor?
class Person:
    def setFullName(self, fName, lName):
        self.fName = fName
        self.lName = lName
    def printFullName(self):
        print(self.fName," ",self.lName)

personName = Person()
personName.setFullName("Sagar","Nangare")
personName.printFullName()
