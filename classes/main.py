# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        if speed < 0  or speed > 1:
            raise Exception("ValueError, speed must be between 0 and 1")
        elif endurance < 0 or endurance > 1:  
            raise Exception("ValueError, endurance must be between 0 and 1")
        elif accuracy < 0 or accuracy > 1:
            raise Exception("ValueError, accuracy must be between 0 and 1")

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."


    def strength(self):

        strenght_tuple = max(self.speed, self.endurance, self.accuracy)
        return strenght_tuple


        # if self.speed > self.endurance and self.speed > self.accuracy:
        #     return ("speed", self.speed)
        # elif self.endurance > self.speed and self.endurance > self.accuracy:
        #     return ("endurance", self.endurance)
        # elif self.accuracy > self.speed and self.accuracy > self.endurance:
        #     return ("accuracy", self.accuracy)
        # elif self.speed > self.endurance and self.speed == self.accuracy:
        #     return ("speed", self.speed, "accuracy", self.accuracy)
        # elif self.speed == self.endurance and self.speed > self.accuracy:
        #     return ("speed", self.speed, "endurance", self.endurance)
        

   


kelly = Player("kelly",0.6,0.6,0.5)
        
print(kelly.strength())