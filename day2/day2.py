strategy_guide = open("input_day2.txt", "r").read().split("\n")

score = 0

win_games={"A Y", "B Z", "C X"}
draw_games={"A X", "B Y", "C Z"}
lose_games={"B X", "C Y", "A Z"}

def win(my_hand):
    if my_hand == "X": return 1+6 # Rock Scissors
    if my_hand == "Y": return 2+6 # Paper Rock
    if my_hand == "Z": return 3+6 # Scissors Paper

def draw(my_hand):
    if my_hand == "X": return 1+3 # Rock Rock
    if my_hand == "Y": return 2+3 # Paper Paper 
    if my_hand == "Z": return 3+3  # Scissors Scissors

def lose(my_hand):
    if my_hand == "X": return 1+0 # Rock Paper
    if my_hand == "Y": return 2+0 # Paper Scissors
    if my_hand == "Z": return 3+0 # Scissors Rock

for game in strategy_guide:

    #game[0] - opponent
    #game[2] - my_hand

    #A for Rock, B for Paper, and C for Scissors
    #X for Rock, Y for Paper, and Z for Scissors

    #1 for Rock, 2 for Paper, and 3 for Scissors) 
    # plus the score for the outcome of the round 
    # (0 if you lost, 3 if the round was a draw, and 6 if you won

    if game.strip() in win_games: score += win(game[2])
    if game.strip() in draw_games: score += draw(game[2])
    if game.strip() in lose_games: score += lose(game[2])

print(score)

