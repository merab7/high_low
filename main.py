from art import logo, vs
from game_data import data
import random
import sys



def play_h_l ():

    comA = random.choice(data)
    comB = random.choice(data)
    game_score = 0 

    def candidates () :

        nonlocal comB
        nonlocal comA
        
        if data.index(comA) != data.index(comB) :
            print(f"{logo}\n\nCompare A: {comA['name']}, {comA['description']}, from {comA['country']}\n\n{vs}\n\n Against B: {comB['name']}, {comB['description']}, from {comB['country']}   ")
        else :
            comB = data[data.index(comB) + 1]  
            print(f"{logo}\n\nCompare A: {comA['name']}, {comA['description']}, from {comA['country']}\n\n{vs}\n\n Against B: {comB['name']}, {comB['description']}, from {comB['country']}   ")
            
    def winning () :
        nonlocal game_score
        game_score += 1
        print(f"\nYou got it right candidate A: {comA['name']} have {comA['follower_count']}M followers and\ncandidate B: {comB['name']} have {comB['follower_count']}M followers\n your socre is : {game_score} ")
        
        
    while True  :
        candidates()

        user_chois = input(f"\nWho has more followers? Type 'A' or 'B':   ").lower()
        if user_chois not in ["a", "b"]:
          print("You only have two option please check your input")
          return play_h_l()
        else :
            if comA['follower_count'] > comB['follower_count'] and user_chois == "a" :
               winning()
               comB = random.choice(data)
               continue
            
            elif comA['follower_count'] < comB['follower_count'] and user_chois == "b" :
                 winning()
                 comA = comB
                 comB = random.choice(data)
                 continue
            else :
               print(f"\nyou was wrang\ncandidate A: {comA['name']} have {comA['follower_count']}M followers and\n candidate B: {comB['name']} have {comB['follower_count']}M followers\n your socre is : {game_score} ")
               break

play_h_l()