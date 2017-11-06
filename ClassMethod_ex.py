class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "cricket player. ":
            print(self.name, " plays cricket")
        elif self.occupation == "actor":
            print(self.name, " shoots a film.")
    def speaks(self):
        print(self.name, " says how are you? ")
sag = Human("Sachin Tendulkar", "cricket player.")
sag.do_work()
sag.speaks()
