class Car:
    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        #self.__updatesoftware()
        self.__name = "supercar"
    
    def drive(self):
        print('Driving')
        print(self.__maxspeed)
    def setspeed(self, speed):
        self.__maxspeed = speed
        print(self.__maxspeed)
##    def __updatesoftware(self):
##        print('Update software')
obj = Car()
obj.drive()
obj.setspeed(100)
