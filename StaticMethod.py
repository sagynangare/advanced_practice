class Students(object):
    total = 0
    def status():
        print("\n Total Number of students is: ",Students.total)
    status=staticmethod(status)
    def __init__(self, name):
        self.name = name
        Students.total +=1
print("Before creating instance: ",Students.total)
student1 = Students('Guido')
student2 = Students('Van')
student3 = Students('Rossum')
Students.status()
student1.staus()
    
