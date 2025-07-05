import random

deck = [1, 2, 3, 4, 5]

"""
'return None' meaning it changes an object in-place
it doesn't return a new deck of cards, only modifies
an existing one
"""
random.shuffle(deck)

for card in deck:
    print(card)
