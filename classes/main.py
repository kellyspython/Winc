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
        if self.speed == self.endurance and self.speed == self.accuracy:
            return ("speed", self.speed, "endurance", self.endurance, "accuracy", self.accuracy) 
            
        elif self.speed > self.endurance and self.speed == self.accuracy:
            return ("speed", self.speed, "accuracy", self.accuracy)
        elif self.speed == self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed, "endurance", self.endurance)
        
        elif self.endurance > self.speed and self.endurance == self.accuracy:
            return ("endurance", self.endurance, "accuracy", self.accuracy)
        elif self.endurance > self.accuracy and self.endurance == self.speed:
            return ("endurance", self.endurance, "speed", self.speed) 

        elif self.accuracy > self.endurance and self.accuracy == self.speed:
            return ("speed", self.speed, "accuracy", self.accuracy)
        elif self.accuracy > self.speed and self.accuracy == self.endurance:
            return ("endurance", self.endurance, "accuracy", self.accuracy)
               
        elif self.speed > self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed)
        elif self.endurance > self.speed and self.endurance > self.accuracy:
            return ("endurance", self.endurance)
        elif self.accuracy > self.speed and self.accuracy > self.endurance:
            return ("accuracy", self.accuracy)
   
kelly = Player("kelly", 0.6, 0.6, 0.6)
monica = Player("monica", 0.4, 0.5, 0.9)

class Commentator:
    def __init__(self, name):
        self.name = name

    # Get information out class Player return sum
    def sum_player(Player):  
        player_name = getattr(Player, "name", 0)
        player_speed = getattr(Player, "speed", 0)
        player_endurance = getattr(Player, "endurance", 0)
        player_accuracy = getattr(Player, "accuracy", 0)
        sum = (player_speed + player_endurance + player_accuracy)
        return sum


    def compare_players(player_1, player_2, strenght):
        
        player_1 = Player()
        player_1_name = getattr(Player, "name", 0)
        player_1_speed = getattr(Player, "speed", 0)
        player_1_endurance = getattr(Player, "endurance", 0)
        player_1_accuracy = getattr(Player, "accuracy", 0)

        player_2 = Player()
        player_2_name = getattr(Player, "name", 0)
        player_2_speed = getattr(Player, "speed", 0)
        player_2_endurance = getattr(Player, "endurance", 0)
        player_2_accuracy = getattr(Player, "accuracy", 0)

        if strenght == "speed":
            print(f"{player_1}, {player_1_speed}")

        print()

ray = Commentator('Ray Hudson')

print(ray.compare_players(kelly, monica, "speed"))