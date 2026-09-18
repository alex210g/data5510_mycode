'''
This is an example of how to create a DeckOfCards object, shuffle it, and deal cards to play a game
'''

from DeckOfCards import * #inherit the DeckOfCards class from the DeckOfCards.py file

deck = DeckOfCards() #initialize a deck of cards



def calc_score(user_hand): #take the user's hand and calculate the score, taking into account the value of aces
    score = 0
    ace_count = 0
    for card in user_hand: #go through each card in user's hand and add up the score, while also counting the number of aces
        score += card.val
        if card.face == "Ace":
            ace_count += 1
    while score > 21 and ace_count > 0:
        score -= 10 #change the value of an ace from 11 to 1
        ace_count -= 1 #ensure an ace is only counted as 1 once, and not multiple times
    return score

play_game = 'y' #initialize the play_game variable

while play_game == 'y': #loop continues as long as the user wants to keep playing; play_game starts as 'y' so the first round runs automatically
    print("Deck before shuffled:\n")
    deck.print_deck()
    deck.shuffle_deck()
    print("Deck after shuffled:\n")
    deck.print_deck()

    card = deck.get_card() 
    print("Your first card is: ", card)
    card2 = deck.get_card()
    print("Your second card is: ", card2)
    user_hand = [] #initialize the user's hand
    user_hand.append(card) #add the first card to the user's hand
    user_hand.append(card2) # add the second card to the user's hand
    score = calc_score(user_hand)
    print("Your score is: ", score)
    
    hit = input("would you like a hit? ")
        
    if hit == 'y': #if the user wants a hit, enter a while loop to keep giving them cards until they either bust or choose to stop
        while True:
            card3 = deck.get_card() #deal the user a new card
            print("Your card is: ", card3)  
            user_hand.append(card3) #add the new card to the user's hand
            score = calc_score(user_hand) #pass the user's hand to the calc_score function to get the new score
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
        dealer_hand = [] #initialize the dealer's hand
        dealer_hand.append(deck.get_card()) #deal the dealer's first card
        print("Dealer's first card: ", dealer_hand[0])
        dealer_hand.append(deck.get_card()) #deal the dealer's second card
        print("Dealer's second card: ", dealer_hand[1])
        dealer_score = calc_score(dealer_hand) #pass dealers hand using the calc_score function to get the dealer's score
        while dealer_score < 17: #makes the dealer hit until they reach a score of 17 or higher
            dealer_hand.append(deck.get_card())
            print("Dealer hits, the card is: ", dealer_hand[-1]) #use negative index to get the last card in the dealer list
            dealer_score = calc_score(dealer_hand)
        print("Dealer score: ", dealer_score)
        if dealer_score > 21: #logic for determining the winner of the game based on the scores of the user and dealer
            print("Dealer busted! You win!")
        elif dealer_score > score:
            print("Dealer wins!")
        elif dealer_score == score:
            print("It's a tie, dealer wins!")
        elif dealer_score < score:
            print("You win!")
    play_game = input("Would you like to play again? (y/n) ") #asks the user if they want to play again
        
print("Thanks for playing!")