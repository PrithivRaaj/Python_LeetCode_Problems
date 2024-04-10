from collections import deque
from typing import List

def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    # Sort the deck in ascending order
    deck.sort()
    
    # Initialize a deque with indices
    indices = deque(range(len(deck)))
    
    # Initialize an array to store the order of revealed cards
    order = [0] * len(deck)
    
    # Iterate through each card in sorted order
    for card in deck:
        # Assign the current card to the index of the first unrevealed card
        order[indices.popleft()] = card
        
        # If there are still unrevealed cards, move the next one to the bottom
        if indices:
            indices.append(indices.popleft())
    
    return order

# Test cases
print(deckRevealedIncreasing([17,13,11,2,3,5,7]))  # Output: [2,13,3,11,5,17,7]
print(deckRevealedIncreasing([1,1000]))           # Output: [1,1000]
