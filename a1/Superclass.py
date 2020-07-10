from typing import Any

class Game:
    """
    The game the players are playing.
    """
    def __init__(self, status: bool) -> None:
        self.current_state = State()
        self.status = status

    def __str__(self) -> str:
        return str(self.status)

    def __eq__(self, other: 'Game') -> bool:
        return self.current_state == other.current_state and self.status == other.status

    def is_over(self, state: 'State') -> bool:
        raise NotImplementedError

    def is_winner(self, player: str) -> bool:
        raise NotImplementedError



class State:
    """

    """
    def __init__(self) -> None:
        self.info = object

    def __str__(self) -> str:
        return str(self.info)

    def __eq__(self, other: Any) -> bool:
        return type(self.info) == other and self.info == other

    def get_current_player_name(self) -> str:
        if self.info == True:
            return 'p1'

    def get_possible_moves(self) -> list:
        """
        return a list of moves that are available
        for players to play
        """
        raise NotImplementedError

    def make_move(self, move: Any) -> 'State':
        """
        Implement the move
        """
        raise NotImplementedError

    def str_to_move(self, move: str) -> Any:
        """
        Return a move that is applicable from string.
        """
        raise NotImplementedError

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether a move is valid.
        """
        raise NotImplementedError
