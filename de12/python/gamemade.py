

import random



deck=[1,2,3,4,5,6,7,8,9,10,11,12,13] * 4

print("ようこそブラックジャックへ")
print("このゲームのルール説明をします。")
print("このゲームは21に近い数の人が勝ちというゲームです")
print("もし、21より大きくなってしまったら、その時点で負けです。")
print("これでルール説明を終わります。ゲームをスタートします！")



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

def result(dealer_hand,player_hand):
    if total(player_hand) > total(dealer_hand):
        print(
            f" \ディーラーの合計は{total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[32mYou Win!\033[0m")

    elif total(dealer_hand) > total(player_hand):  
        print(
            f"\nディーラーの合計は{total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[32mYou Lose...\033[0m" ) 



def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"ディーラーのカードは{dealer_hand[0]}です。")   
    print(f"プレイヤーのカードは{player_hand} 合計が {total(player_hand)}です。")        

    choice = 0


    while choice != quit:
        choice = input("もう一枚引きますか？　それとも引きませんか？ (hit/stand): ").lower()
        if choice == "hit":
            hit (player_hand)
            print(
                f"\nあなたに {player_hand [-1]}が配られ、カードは　{player_hand} 合計は {total(dealer_hand)}です。")
            if total(player_hand)  > 21:
                print("あなたは 21 をこえてしまいました。\033[91mYou Lose...\033[0m")  
                choice = quit


        
             

        elif choice == "stand":
            print(
                f"\nディーラーの2枚目のカードは {dealer_hand[1]}合計は {total(dealer_hand)}です。")
            while total(dealer_hand)  <17:
                hit(dealer_hand)
                print(
                    f"\nディーラーに {dealer_hand[-1]}が配られ、カードは {dealer_hand} 合計は{total(dealer_hand)}です。")
                if total(dealer_hand) > 21:
                    print("ディーラーは21 をこえてしまいました。\033[32mYou Win!!\033[0m")   
                    choice = quit


            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)    
                choice = quit



game()                  














