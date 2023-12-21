import sys
import random as rdm
from enum import Enum

def guess(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_guess():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class GUESS(Enum):
            CHOICE_1 = 1
            CHOICE_2 = 2
            CHOICE_3 = 3

        playerChoice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3")

        if playerChoice not in ['1', '2', '3']:
            print(f"\n{name}, please enter 1, 2, or 3")
            return play_guess
        
        player = int(playerChoice)

        computerChoice = rdm.choice("123")

        computer = int(computerChoice)

        print(f"\n{name} chose {str(GUESS(player)).replace('GUESS.', '').title()}")

        


