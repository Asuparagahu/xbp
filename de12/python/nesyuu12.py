for i in range(1,5):
    print(i,"人目")

import random



deck=[1,2,3,4,5,6,7,8,9,10,11,12,13] * 4

print("ようこそブラックジャックへ")
print("参加する人数を選んでください")



def deal ():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card ="J"
        if card == 12:
            card ="Q" 
        if card == 13:
            card ="K"  
        if card == 1:
            card =  "A"    
        hand.append(card)  
    return hand



def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card ="J"
    if card == 12:
        card ="Q"  
    if card == 13:
        card ="K"  
    if card == 1:   
        card ="A"   
    hand.append(card)
    return hand


def total(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card =="K":
            score = score + 10
        elif card == "A":
            if score >= 11:
                score =score + 1
            else:
                 score += 11
        else:
            score += card
    return score



def play_again():
    again = input("もう一度チャレンジしますか？(Y/N):")    
    if again == "Y"   or again =="y":

        return
    else:
        print("遊んでくれてありがとう！！！")    
        exit()

            














