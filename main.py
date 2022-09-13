import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(player_hand):
  if sum(player_hand) > 21 and 11 in player_hand:
    player_hand.remove(11)
    player_hand.append(1)
  return sum(player_hand)

def dealer_play(player_hand):
  while sum(player_hand) < 16:
      player_hand.append(deal_card())
      calculate_score(player_hand)
  return player_hand

def determine_winner(user_hand, dealer_hand):
  user_score = calculate_score(user_hand)
  dealer_score = calculate_score(dealer_hand)  

  print(f'This is the final user hand {user_hand}. Sum of the user\'s hand {user_score}')
  print(f'This is the final dealer hand {dealer_hand}. Sum of the dealer\'s hand {dealer_score}')
  
  if dealer_score == 21:
    print('Computer wins.')
  elif user_score == 21 and dealer_score != 21:
    print('Blackjack, you win!')
  elif user_score > 21:
    print('You lose.')
  elif dealer_score > 21:
    print('You win.')
  elif user_score < dealer_score:
    print('You lose.')
  elif user_score > dealer_score:
    print('You win.')
  elif user_score == dealer_score:
    print('It is a tie')

def playing():
  user_hand = []
  dealer_hand = []
  game_in_play = True
  
  for i in range(2):
    user_hand.append(deal_card())
    dealer_hand.append(deal_card())
  
  while game_in_play:
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)  
  
    print(f'This is the user hand {user_hand}. Sum of the user\'s hand {user_score}')
    print(f'This is the dealer\'s first card {dealer_hand[0]}.\n')
    
    if user_score >= 21 or dealer_score == 21:
      game_in_play = False
    else:
      get_card = input('Type "Y" to get another card or "N" to pass: ')
      if get_card == "Y":
        user_hand.append(deal_card())
      else:
        game_in_play = False

  dealer_play(dealer_hand)
  determine_winner(user_hand, dealer_hand)

while input('\nDo you want to play a game of Blackjack? Type "Y" or "N": ') == "Y":
  clear()
  print(logo)
  playing()
else:
  print('Next time then')
  
