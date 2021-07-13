import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['p','r','s'])
    
    if user == computer :
        print("It's a tie")
        return play()
    
    if is_win(user, computer):
        return "You won"
    return "You lost"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())