import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
  thisCard = deckListIn.pop()
  return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
  deckListOut = deckListIn.copy() # Deep Copy: Different from deckListIn[:]
  random.shuffle(deckListOut)
  return deckListOut

# Main code
print(f'Welcome to Higher or Lower \n'
      f'You have to choose whether the next card to be shown will be higher or lower than the current card \n'
      f'Getting it right adds 20 points; get it wrong and you \n'
      f'lose 15 points. \n'
      f'You have 50 points to start. \n'
      f'\n')

# Create a list of Dictionary
startingDeckList = []

for suit in SUIT_TUPLE:
  for thisValue, rank in enumerate(RANK_TUPLE):
    cardDict = {'rank': rank, 'value': thisValue+1, 'suit': suit}
    startingDeckList.append(cardDict)


score = 50
while True:
  print()
  gameDeckList = shuffle(startingDeckList)
  currentCardDict = getCard(gameDeckList)
  currentCardRank = currentCardDict['rank']
  currentCardValue = currentCardDict['value']
  currentCardSuit = currentCardDict['suit']
  print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
  print()

  # play 1 game of 8 cards

  for cardNumber in range(0, NCARDS): # play one game of this many cards
    answer = input(f'Will the next card be higher or lower than the {currentCardRank} of '
                   f'{currentCardSuit}?  (enter h or l):')
    answer = answer.casefold()

    nextCardDict = getCard(gameDeckList)
    nextCardRank = nextCardDict['rank']
    nextCardSuit = nextCardDict['suit']
    nextCardValue = nextCardDict['value']
    print(f'Next card is: {nextCardRank} of {nextCardSuit}')

    if answer == 'h':
      if nextCardValue > currentCardValue:
        print('You got it right, it was higher')
        score = score + 20
      else:
        print('Sorry, it was not higher')
        score = score - 15
    elif answer == 'l':
      if nextCardValue < currentCardValue:
        score = score + 20
        print('You got it right, it was lower')
      else:
        score = score - 15
        print('Sorry, it was not lower')

    print('Your score is:', score)
    print()
    currentCardRank = nextCardRank
    currentCardValue = nextCardValue  # don't need current suit

  goAgain = input('To play again, press ENTER, or "q" to quit: ')
  if goAgain == 'q':
    break

exit()

