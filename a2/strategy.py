"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""

from game import Game
from game_state import GameState


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Game) -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Game) -> str:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


# TODO: Implement a recursive version of the minimax strategy.
def recursive_minimax_strategy(game: Game) -> str:
    """
    Return a move for game through recursion.
    """
    ori_state = game.current_state
    player = game.current_state.get_current_player_name()
    moves = []
    for move in game.current_state.get_possible_moves():
        # print(move)
        next_state = ori_state.make_move(move)
        # game.current_state = next_state
        moves.append((move, recursive_minimax_score(game, next_state, player)))
    print(moves)
    h_score = max([mov[1] for mov in moves])
    for mo in moves:
        # print(mo)
        if mo[1] == h_score:
            return mo[0]


def recursive_minimax_score(game: Game, state: GameState, player: str) -> int:
    """
    Return the score for each possible move.
    """

    if game.is_over(state):
        return 1 * (check_over_score(game, state, player))
    moves = state.get_possible_moves()
    for move in moves:
        next_state = state.make_move(move)
        score = recursive_minimax_score(game, next_state, player)
        if score == 1:
            return score
        elif score == 0:
            return score
    return -1


def check_over_score(game: Game, state: GameState, player: str) -> int:
    """
    Return the score for a game that is over
    Precondition: game.is_over(state) is True
    """

    game.current_state = state
    # player = game.current_state.get_current_player_name()
    players = ['p1', 'p2']
    players.remove(player)
    assert len(players) == 1
    if game.is_winner(player):
        return 1
    elif game.is_winner(players[0]):
        return -1
    return 0


# TODO: Implement an iterative version of the minimax strategy.
class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None, score=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        self.children = children[:] if children is not None else []
        self.score = score


def iterative_minimax_score(game: Game, state: GameState)-> str:
    """
    Return a score for game at state.
    """
    stack = []
    # current_state = game.current_state
    first = Tree(state)
    stack.append(first)
    while stack:
        out = stack.pop()
        current_state = out.value
        if game.is_over(current_state):
            player = current_state.get_current_player_name()
            out.score = check_over_score(game, current_state, player)
        else:
            if not out.children:
                moves = out.value.get_possible_moves()
                for move in moves:
                    out.children.append(Tree(out.value.make_move(move)))
                stack.append(out)
                for new_state in out.children:
                    if new_state.score is None:
                        stack.append(new_state)
            else:
                scores = []
                for new_s in out.children:
                    player = new_s.value.get_current_player_name()
                    scores.append(-1 * check_over_score
                    (game, new_s.value, player))
                    out.score = max(scores)
    return first.score


def iterative_minimax(game: Game) -> str:
    """
    Return a strategy for game using iterative_minimax
    """
    movements = []
    current_state = game.current_state
    moves = current_state.get_possible_moves()
    for move in moves:
        next_state = current_state.make_move(move)
        score = iterative_minimax_score(game, next_state)
        if score == -1:
            return move
        else:
            movements.append((move, score))
    scores = []
    for movement in movements:
        scores.append(movement[1])
    for movement in movements:
        if movement[1] == max(scores):
            return movement[0]


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    # # s = SubtractSquareGame(True)
    # # s1 = s.current_state.make_move(1)
    # # s2 = s.current_state.make_move(4)
    # # s3 = s.current_state.make_move(9)
    # # iterative_minimax_score(s, s1)
    # h = Stonehenge(True)
    # h1 = h.current_state.make_move('A')
    # h2 = h1.make_move('F')
    # h3 = h1.make_move('D')
    # h.current_state = h3
    # recursive_minimax_score(h, h3, 'p2')
