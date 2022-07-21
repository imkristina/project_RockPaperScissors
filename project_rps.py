import random

def play(): 
    #play() is the game
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n") 
    computer = random.choice(['r', 'p', 's'])

    if user == computer: 
        return 'Womp, Womp... its a TIE'
         #rules of the game: (r > s, s > p, p > r)
    
    if is_win(user, computer):
        return 'Winner Winner, Chicken Dinner!!'

        return 'Dont quit your day job!'
        #no if stmt needed because there are no other options. 

def is_win(player, opponent):
    #return true if player wins (r > s, s > p, p > r)

    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
