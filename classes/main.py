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
            
        if self.speed > self.endurance and self.speed == self.accuracy:
            return ("speed", self.speed, "accuracy", self.accuracy)
        if self.speed == self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed, "endurance", self.endurance)
        
        if self.endurance > self.speed and self.endurance == self.accuracy:
            return ("endurance", self.endurance, "accuracy", self.accuracy)
        if self.endurance > self.accuracy and self.endurance == self.speed:
            return ("endurance", self.endurance, "speed", self.speed) 

        if self.accuracy > self.endurance and self.accuracy == self.speed:
            return ("speed", self.speed, "accuracy", self.accuracy)
        if self.accuracy > self.speed and self.accuracy == self.endurance:
            return ("endurance", self.endurance, "accuracy", self.accuracy)
               
        if self.speed > self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed)
        if self.endurance > self.speed and self.endurance > self.accuracy:
            return ("endurance", self.endurance)
        if self.accuracy > self.speed and self.accuracy > self.endurance:
            return ("accuracy", self.accuracy)



class Commentator:
    def __init__(self, name):
        self.name = name

    # Get information out class Player return sum
    def sum_player(self, Player):  
        player_name = getattr(Player, "name", 0)
        player_speed = getattr(Player, "speed", 0)
        player_endurance = getattr(Player, "endurance", 0)
        player_accuracy = getattr(Player, "accuracy", 0)
        sum = (player_speed + player_endurance + player_accuracy)
        return sum


    def compare_players(self, player_1, player_2, attr):
        p_1_name = getattr(player_1, "name")
        p_1_attr = getattr(player_1, attr)
        p_2_name = getattr(player_2, "name")
        p_2_attr= getattr(player_2, attr)
        if p_1_attr > p_2_attr:
            return p_1_name
        elif p_1_attr == p_2_attr:
            sum_p1 = Commentator.sum_player(self, player_1)
            sum_p2 = Commentator.sum_player(self,player_2)
            if sum_p1 > sum_p2:
                return p_1_name
            else:
                return p_2_name
        else:
            return p_2_name
       
kelly = Player("kelly", 0.4, 0.3, 0.6)
monica = Player("monica", 0.4, 0.5, 0.9)
ray = Commentator('Ray Hudson')

print(ray.compare_players(kelly, monica, "speed"))