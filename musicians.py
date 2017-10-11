class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["boom", "thump", "ding"])
        
    def count(self, start_at):
        for n in range(1,start_at):
            print (n)

    def combust(self):
        print("I am combusting now")
        

class Band(Musician):
    
    def __init__(self):
        self.members = []
    
    def hire(self, instrument, name):
        wanted =[Guitarist, Drummer, Bassist]
        name = input("What is the new members name?")
        instrument = input("What kind of instrument do they play?")
        if instrument not in wanted:
            print("We aren't looking for that type of musician right now")
        else:
            self.members.append(instrument, name)
    
    def fire(self, instrument, name):
        if name in self.members:
            self.members.remove(instrument, name)
            
    def play(self, start_at, duration):
        if Drummer in self.members:
            self.Drummer.count(self, start_at)
            for instrument in self.members:
                self.insturment.solo(self, duration)