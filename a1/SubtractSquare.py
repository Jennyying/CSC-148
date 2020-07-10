"""
SubtractSquare
"""
from typing import Any
from Superclass import Game
from Superclass import State


class SubtractSquare(Game):
    """
    Choosing a number, the game keeps subtracting the square of
    positive numbers until the final value is 0.

    status: whether the game has started
    current_state: the state of the game.
    """

    def __init__(self, status: bool) -> None:
        """
        Initialize the game SubtractSquare.
        Taking status to start the game.
        Initialize its current state by taking a square.
        """
        print('Choose a positive number to substract from the value. ')
        Game.__init__(self, status)
        self.current_state = SubtractSquareState(int(input()))

    def __str__(self) -> str:
        """
        Return a string representation of SubtractSquare.
        """
        return 'The current number is ' + str(self.current_state.info)

    def __eq__(self, other: int) -> bool:
        """
        Return whether the game has the same state as other.
        """
        return self.current_state == other

    def get_instructions(self) -> str:
        """
        Return a string that states the instructions
        """
        return 'A positive number is choosen \
by player as starting value. \
The player whose turn it is choose a square of positive \
number that is less than the starting value. \
After subtracting, we get a new value, and the next player chooses a value \
to subtract from it. The game continues until no move is possible. \
Whoever is about to play loses the game.'

    def is_over(self, state: 'SubtractSquareState') -> bool:
        """
        Return whether the game is over.
        """
        return int(state.info) == 0

    def is_winner(self, player: str) -> bool:
        """
        Return whether player is the winner of the game.
        """
        over = self.is_over(self.current_state)
        if self.current_state.user == player:
            return over and False
        return over and True

    def str_to_move(self, move: str) -> int:
        """
        convert move to int such that the methods can use directly.
        """
        return int(move)


class SubtractSquareState(State):
    """
    The state of the game SubtractSquare.

    info: the current number
    user: the person who is currently playing.
    """
    def __init__(self, number: int) -> None:
        self.info = number
        self.user = 'p1'

    def __str__(self) -> str:
        return 'Current state is ' + str(self.info)

    def __eq__(self, other: Any) -> bool:
        return type(self.info) == other and self.info == other

    def get_current_player_name(self) -> str:
        """
        Return which player is playing right now.
        """
        current_name = self.user
        return current_name

    def get_possible_moves(self) -> list:
        """
        Return all the squares of numbers
         that can be subtracted from current value.
        >>> state = SubtractSquareState(15)
        >>> state.get_possible_moves()
        [1, 4, 9]
        """
        moves = []
        number = int(self.info)
        if number != 1:
            for i in range(0, number):
                if i != 0 and i ** 2 <= number:
                    moves.append(i ** 2)
        elif number == 1:
            moves = [1]
        return moves

    def make_move(self, move: int) -> 'SubtractSquareState':
        """
        Return the state after move has been applied.
        >>> state = SubtractSquareState(15)
        >>> new_s = state.make_move(4)
        >>> new_s.info
        11
        """
        names = ['p1', 'p2']
        names.remove(self.user)
        current = int(self.info)
        new_info = current - move
        new = SubtractSquareState(new_info)
        new.user = names[0]
        return new

    def is_valid_move(self, move: int) -> bool:
        """
        Return whether move can be applied to state.
        >>> state = SubtractSquareState(23)
        >>> state.is_valid_move(25)
        False
        """
        return move in self.get_possible_moves()


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
    import doctest
    doctest.testmod()
