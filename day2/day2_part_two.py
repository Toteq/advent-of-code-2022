strategy_guide = open("input_day2.txt", "r").read().split("\n")

score = 0

def win(opponent):
    if opponent == "A": return 2+6 # Rock Paper
    if opponent == "B": return 3+6 # Paper Scissors
    if opponent == "C": return 1+6 # Scissors Rock

def draw(opponent):
    if opponent == "A": return 1+3 # Rock Rock
    if opponent == "B": return 2+3 # Paper Paper
    if opponent == "C": return 3+3 # Scissors Scissors

def lose(opponent):
    if opponent == "A": return 3+0 # Rock Scissors
    if opponent == "B": return 1+0 # Paper Rock
    if opponent == "C": return 2+0 # Scissor Paper

for game in strategy_guide:

    #A for Rock, B for Paper, and C for Scissors
    #X for Rock, Y for Paper, and Z for Scissors

    #1 for Rock, 2 for Paper, and 3 for Scissors) 
    # plus the score for the outcome of the round 
    # (0 if you lost, 3 if the round was a draw, and 6 if you won

    #the second column says how the round needs to end:
    #  X means you need to lose,
    #  Y means you need to end the round in a draw,
    #  Z means you need to win.

    if game.strip()[2] == "X": score += lose(game[0])
    if game.strip()[2] == "Y": score += draw(game[0])
    if game.strip()[2] == "Z": score += win(game[0])

print(score)

