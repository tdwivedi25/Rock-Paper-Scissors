import random, math

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)
    
    #r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)
    
    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


def play_best_of(n =int(input("How many best of games would you like to play?:" ))):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7) 
    
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        # tie
        result, user, computer = play()
        if result == 0:
            print("It is a tie, You and the computer have both chosen {}. ".format(user))
        # you win
        elif result == 1:
            player_wins +=1
            print("You chose {} and the computer chose {}. You won!".format(user, computer))
        else:
           computer_wins += 1
           print('You chose {} and the computer chose {}. You lost!'.format(user, computer)) 
        
    if player_wins > computer_wins:
        print("Congrats! You have won the best of {} of games!".format(n))

    else:
        print('Unfortunately, the computer has won the best of {} games. Better luck next time!'.format(n))
    
if __name__ == '__main__':
    play_best_of()