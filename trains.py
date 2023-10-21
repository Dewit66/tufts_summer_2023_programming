from turtle import up


yes = True
Yes = True
No = False
no = False


class Train:
    def __init__(self,ns):
        self.train_on = True
        self.number = int(input("Number?\n"))
        self.capacity = int(input("train capacity:\n"))
        self.stops = []
        for i in range(ns):
            s = str(i + 1)
            stups = str(input("what is stop " + s + " name?\n"))
            
            self.stops.append(stups)

        self.direction = ("up","down")
        self.cur_stop = None

    def test(self):
        # print(self.stops)
        pass

    def move(self):
        train_on = True
        while train_on:
            direction = self.direction[0]
            while direction == "up":
                for i in range(len(self.stops)):
                    self.cur_stop = self.stops[i]
                    if self.stops[i + 1] != None:
                        train_on = bool(input("Trains still on:\n"))
                        direction = self.direction[1] 

            while direction == "down":
                for i in reversed(range(len(self.stops))):
                    self.cur_stop = self.stops[i]
                    if self.stops[i - 1] != None:


    def stop(self):
        pass
    

    def occupancy(self):
        pass



class Passenger:
    def __init__(self,nam,embark,disbark):
        self.name = nam
        self.embarking_stop = embark
        self.disembarking_stop = disbark
    
    def embarking(self):
        pass

    def disembarking(self):
        pass
    

ns = int(input("How many stops?\n"))
o = Train(ns)
o.move()

