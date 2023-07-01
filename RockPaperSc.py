import random

def play():
    user=input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer=random.choice(['r','p','s'])
    print(f"the CPU played {computer}")
    if user==computer:
        return "draw"
    elif isWin(user, computer):
        return "you won"
    else:
        return "you lost"
        


def isWin(player, oponent):
    if (player=='r' and oponent=='s') or (player=='s' and oponent=='p') or (player=='p' and oponent=='r') :
        return True
    else:
        return False

print(play())




