"""
Game Chopsticks
"""
import copy
from typing import Any
from Superclass import Game
from Superclass import State


class ChopsticksGame(Game):
    """
    A game with each of the two players having one finger up
    on each hand. Players take turns to touch the other player's
    hand, increasing the number of fingers being up by the number
    of their own hands. If one player has both of hands with number
    five(zero), he loses the game.

    """

    def __init__(self, status: bool) -> None:
        Game.__init__(self, status)
        self.current_state = ChopState((1, 1, 1, 1), 'p1')

    def __str__(self) -> str:
        return 'The current state is ' + str(self.current_state.info)

    def __eq__(self, other: 'ChopsticksGame') -> bool:
        return self.current_state == other.current_state

    def get_instructions(self) -> str:
        """
        Return a string that states the instructions

        >>> ch = ChopsticksGame(True)
        >>> ch.get_instructions()
        'Each of the player has one\
finger points up at the beginning. \
Player A touches one hand to one hand of Player B, increasing the number \
of fingers pointing up on the hand of Player B \
by the number of fingers point up \
on the hand of Player A. Player A and Player B \
take turns.If one hand has five \
fingers point up, it becomes dead. \
The game continues until one player has two \
dead hands, and thus lose.'
        """
        return 'Each of the player has one\
finger points up at the beginning. \
Player A touches one hand to one hand \
of Player B, increasing the number \
of fingers pointing up on the hand of Player B \
by the number of fingers point up \
on the hand of Player A. Player A and Player B \
take turns.If one hand has five \
fingers point up, it becomes dead. \
The game continues until one player has two \
dead hands, and thus lose.'

    def is_over(self, state: 'ChopState') -> bool:
        """
        Return whether the game is over.

        >>> ch = ChopsticksGame(True)
        >>> ch.is_over(ch.current_state)
        False
        """
        value = state.info
        return (value[0] == 0 and value[1] == 0)\
               or (value[2] == 0 and value[3] == 0)

    def is_winner(self, player: str) -> bool:
        """
        Return whether player is the winner of the game.
        >>> ch = ChopsticksGame(True)
        >>> ch.current_state.info = (0, 0, 3, 4)
        >>> ch.is_winner('p1')
        False
        """
        over = self.is_over(self.current_state)
        value = self.current_state.info
        if player == 'p1':
            return over and value[2] == 0 and value[3] == 0
        return over and value[0] == 0 and value[1] == 0

    def str_to_move(self, move: str) -> str:
        """
        convert move to a move that can be produced by get_possible_moves.
        >>> ch = ChopsticksGame(True)
        >>> ch.str_to_move('ll')
        'll'
        """
        return move


class ChopState(State):
    """
    The state of the class ChopsticksGame, a subclass of State.
    """
    def __init__(self, info: tuple, player: str) -> None:
        self.info = info
        self.user = player

    def __str__(self) -> str:
        return 'Player 1 is ' + str(self.info[0]) +\
               ' - ' + str(self.info[1]) + ' player 2 is ' + \
               str(self.info[2]) + ' - ' + str(self.info[3])

    def __eq__(self, other: Any) -> bool:
        return type(self.info) == other and self.info == other

    def get_current_player_name(self) -> str:

        """
        Return which player is playing right now.

        >>> chs = ChopState((1, 1, 1, 1), 'p1')
        >>> chs.get_current_player_name()
        'p1'
        """
        current_name = self.user
        return current_name

    def get_possible_moves(self) -> list:
        """
        Return all the squares of numbers
         that can be subtracted from current value.

        >>> chs = ChopState((1, 1, 1, 1), 'p1')
        >>> chs.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        """
        eve = ['ll', 'lr', 'rl', 'rr']
        if self.user == 'p1':
            if self.info[0] == 0:
                eve.remove('ll')
                eve.remove('lr')
            if self.info[1] == 0:
                eve.remove('rl')
                eve.remove('rr')
        elif self.user == 'p2':
            if self.info[2] == 0:
                eve.remove('ll')
                eve.remove('lr')
            if self.info[3] == 0:
                eve.remove('rl')
                eve.remove('rr')
        return eve

    def make_move(self, move: str) -> 'ChopState':
        """
        Return the state after move has been applied.

        >>> chs = ChopState((1, 1, 1, 1), 'p1')
        >>> move = 'lr'
        >>> new_chs = chs.make_move(move)
        >>> new_chs.info
        (1, 1, 1, 2)
        """
        l = ['p1', 'p2']
        l.remove(self.user)
        l1 = copy.deepcopy(self.info[0])
        r1 = copy.deepcopy(self.info[1])
        l2 = copy.deepcopy(self.info[2])
        r2 = copy.deepcopy(self.info[3])
        new = []
        if self.user == 'p1':
            if move == 'll':
                new = [l1, r1, l2 + l1, r2]
            elif move == 'lr':
                new = [l1, r1, l2, r2 + l1]
            elif move == 'rl':
                new = [l1, r1, l2 + r1, r2]
            elif move == 'rr':
                new = [l1, r1, l2, r2 + r1]
        elif self.user == 'p2':
            if move == 'll':
                new = [l1 + l2, r1, l2, r2]
            elif move == 'lr':
                new = [l1, r1 + l2, l2, r2]
            elif move == 'rl':
                new = [l1 + r2, r1, l2, r2]
            elif move == 'rr':
                new = [l1, r1 + r2, l2, r2]
        result = []
        for item in new:
            if item > 5:
                result.append(item - 5)
            elif item == 5:
                result.append(0)
            else:
                result.append(item)
        new_move = (result[0], result[1], result[2], result[3])
        new = ChopState(new_move, l[0])
        return new

    def is_valid_move(self, move: tuple) -> bool:
        """
        Return whether move can be applied to state.

        >>> chs = ChopState((1, 1, 1, 1), 'p1')
        >>> move = 'll'
        >>> move in chs.get_possible_moves()
        True

        """
        return move in self.get_possible_moves()


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
    import doctest
    doctest.testmod()
