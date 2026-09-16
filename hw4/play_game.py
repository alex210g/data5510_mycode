'''
This is an example of how to create a DeckOfCards object, shuffle it, and deal cards to play a game
'''

from DeckOfCards import *

deck = DeckOfCards()
deck.print_deck()
deck.shuffle_deck()
deck.print_deck()


def calc_score(user_hand):
    score = 0
    ace_count = 0
    for card in user_hand:
        score += card.val
        if card.face == "Ace":
            ace_count += 1
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score


while True:
    play_again = input("would you like to play again? ")
    if play_again == 'y':
        deck.shuffle_deck()
        while True: 
            if play_again != 'n':
                card = deck.get_card()
                card2 = deck.get_card()
                user_hand = []
                user_hand.append(card)
                user_hand.append(card2)
                score = calc_score(user_hand)
                print("Your score is: ", score)
                
                hit = input("would you like a hit? ")
                
                if hit == 'y':
                    while True:
                        card3 = deck.get_card()
                        user_hand.append(card3)
                        score = calc_score(user_hand)
                        print("new score: ", score)

                        if score > 21:
                            print("You busted!")
                            break
                        else:
                            hit = input("would you like a hit? ")
                            if hit != 'y':
                                break
                if score <= 21:
                    print("final score: ", score)
                    dealer_hand = []
                    dealer_hand.append(deck.get_card())
                    dealer_hand.append(deck.get_card())
                    dealer_score = calc_score(dealer_hand)
                    while dealer_score < 17:
                        dealer_hand.append(deck.get_card())
                        dealer_score = calc_score(dealer_hand)
                    print("Dealer score: ", dealer_score)
                    if dealer_score > 21:
                        print("Dealer busted! You win!")
                    elif dealer_score > score:
                        print("Dealer wins!")
                    elif dealer_score == score:
                        print("It's a tie, dealer wins!")
                    elif dealer_score < score:
                        print("You win!")
                    break
            else:
                break
    else:
        break

        
