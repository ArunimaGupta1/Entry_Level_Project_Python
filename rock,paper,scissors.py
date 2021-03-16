import random
def is_win(player,opponent):
    #return true if player wins
    #r>s ,s>p ,p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play():
    user = input("What's your choice? Enter 'r' for rock, 's' for scissors and 'p' for paper\n")
    computer = random.choice(['r','s','p'])
    if user == computer:
        return 'It is a tie'

    #r>s, s>p, p>r
    if is_win(user,computer):
        return 'You win!!!'

    return 'You lost'

