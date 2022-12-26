# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_score_one = "Ruud Gullit"
player_score_two = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_score_one + " " + str(goal_0) + " " + player_score_two + " " + str(goal_1)
report = player_score_one + " scored in the " + str(goal_0) + "nd minute\n" + player_score_two + " scored in the " + str(goal_1) + "th minute"

player = "Ruud Gullit"
find_space = player.find(" ")

first_name = player[:find_space]
last_name = player[find_space:]

last_name_len = len(last_name)
name_short = f"{first_name[0]}. {last_name}"

chant_met_space = f"{first_name}! "* len(first_name)
chant_count = len(chant_met_space)
chant = chant_met_space[:-1]

good_chant = chant[:-1]!=""


