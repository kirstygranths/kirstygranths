import random

#MOVES
player_score = 0
computer_score = 0
print('Rock, Paper Scissors. Best out of 3 rounds.')

actions = ["Rock", "Paper", "Scissors"]

for game in range(3):
    computer_move = random.choice(actions)
    player_move = input('Rock, Paper, Scissors?').capitalize().rstrip()

#OUTCOMES
    if player_move not in actions:
        raise ValueError('Move not valid. Please select Rock, Paper, Scissors')
        player_move = input('Rock, Paper, Scissors?')
    else:
        print(f'You played: {player_move}')
        print(f'Computer played: {computer_move}')
        if player_move == "Rock" and computer_move == "Scissors":
            print(f'You win with {player_move}.')
            player_score = player_score + 1
            print(f'Player score:{player_score}')
        elif player_move == "Scissors" and computer_move == "Paper":
            print(f'You win with {player_move}.')
            player_score = player_score + 1
        elif player_move == "Paper" and computer_move == "Rock":
            print(f'You win with {player_move}.')
            player_score = player_score + 1
        elif computer_move == "Rock" and player_move == "Scissors":
            print(f'You lose. Computer wins with {computer_move}.')
            computer_score = computer_score + 1
        elif computer_move == "Scissors" and player_move == "Paper":
            print(f'You lose. Computer wins with {computer_move}.')
            computer_score = computer_score + 1
        elif computer_move == "Paper" and player_move == "Rock":
            print(f'You lose. Computer wins with {computer_move}.')
            computer_score = computer_score + 1
        else:
            print('Draw!')
    print(f'Player score:{player_score}\nComputer score:{computer_score}\n')

if player_score > computer_score:
    print(f'End of game, Player wins with {player_score} points!')
if computer_score > player_score:
    print(f'End of game, Computer wins with {computer_score} points!')
else:
    print(f'End of game - its a draw!')
