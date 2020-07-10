"""
Strategy
"""
from random import randint
from typing import Any
from ChopsticksGame import ChopsticksGame
from Superclass import Game, State


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

# TODO: Implement a random strategy.
def random_strategy(game: Game) -> str:
    """
    Return a random move for game.
    """
    moves = game.current_state.get_possible_moves()
    if type(game) == ChopsticksGame:
        return moves[randint(0, len(moves) - 1)]
    return moves[-1]

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
