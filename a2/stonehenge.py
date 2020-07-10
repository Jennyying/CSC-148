"""
An implementation of Stonehenge
"""
import copy
from typing import Any
from game import Game
from game_state import GameState


class Stonehenge(Game):
    """
    Abstract class for a game to be played with two players.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.

        :param p1_starts: A boolean representing whether Player 1 is the first
                          to make a move.
        :type p1_starts: bool
        """
        self.status = p1_starts
        length = int(input("Enter the number "
                           "to form a hexagonal with sidelength you entered: "))
        self.current_state = StonehengeState(p1_starts, length)

    def __str__(self) -> str:
        """
        Return a string representation of Stonehenge.
        """
        return 'The current state is ' + str(self.current_state.info)

    def __eq__(self, other: 'Stonehenge') -> bool:
        """
        Return whether the game has the same state as other.
        """
        return self.current_state == other.current_state

    def get_instructions(self):
        """
        Return the instructions for this Game.

        :return: The instructions for this Game.
        :rtype: str
        """
        return 'Players take turns claming cells' + \
            ' When a player captures at least half ' \
            'of the cells in a lay line, ' + \
            'then the player caputres the lay line. ' \
            'The first player captures ' + \
            'half of the laylines win'

    def is_over(self, state) -> bool:
        """
        Return whether or not this game is over.

        :return: True if the game is over, False otherwise.
        :rtype: bool

        """
        # Count the number of '@' innitially
        # Count the number of '@' innitially
        status = False
        if state.get_current_player_name() == 'p1':
            status = True
        n = 0
        s = StonehengeState(status, state.length)
        for li in s.info:
            for ele in li:
                if ele == '@':
                    n += 1
        # Count the number of leylines claimed in current state.
        n1 = 0
        n2 = 0
        i = 1
        for ele in state.info[0]:
            if ele == '1':
                n1 += 1
            elif ele == '2':
                n2 += 1
        while i != state.length + 2:
            if state.info[i][0] == '1':
                n1 += 1
            if state.info[i][0] == '2':
                n2 += 1
            if state.info[i][-1] == '1' and i != state.length:
                n1 += 1
            if state.info[i][-1] == '2' and i != state.length:
                n2 += 1
            i += 1
        for ele in state.info[-1]:
            if ele == '1':
                n1 += 1
            elif ele == '2':
                n2 += 1
        if n1 >= 1 / 2 * n or n2 >= 1 / 2 * n:
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :param player: The player to check.
        :type player: str
        :return: Whether player has won or not.
        :rtype: bool
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return an invalid move.

        """
        return string


class StonehengeState(GameState):
    """
    The state of the game SubtractSquare.

    length: the number of lines in the last line
    info: the current number
    user: the person who is currently playing.
    board: the str representation of the game state
    """
    def __init__(self, is_p1_turn, number: int) -> None:
        """
        Initialize the game

        >>> s = StonehengeState(True, 2)
        >>> s.info
        [['@', '@'], ['@', 'A', 'B', '@'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G', '@'], ['@', '@']]
        >>> s = StonehengeState(True, 1)
        >>> s.info
        [['@', '@'], ['@', 'A', 'B'], ['@', 'C', '@'], ['@']]

        """
        self.length = number
        super().__init__(is_p1_turn)
        self.turn = is_p1_turn
        # self.user = 'p1'
        old = ['C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        self.info = [["@", '@'], ['@', 'A', 'B', '@']]
        new = ['@']

        i = 1
        while i != number:
            a = ['@']
            j = 0
            while j != (i + 2):
                a.append(old[j])
                j += 1
            for item in a:
                if item != '@':
                    old.remove(item)
            if i != number - 1:
                a.append('@')
            self.info.append(a)
            i += 1
        k = 0
        while k != number:
            new.append(old[k])
            k += 1
        new.append('@')
        self.info.append(new)
        b = []
        n = 0
        while n != number:
            b.append('@')
            n += 1
        self.info.append(b)
        if self.length == 1:
            self.info[1].pop()

    def __str__(self) -> str:
        """
        Return a string representation of Stonehenge
        """
        info = self.info
        start = '      ' + str(info[0][0]) + '   ' \
                + str(info[0][1]) + '\n' + '     /   /' + '\n' + \
                str(info[1][0]) + ' - ' + str(info[1][1]) + \
                ' - ' + str(info[1][2])
        if self.length == 1:
            return start + '\n' + \
                   '     \\ / \\' + '\n' + \
                   '  ' + str(info[2][0]) + ' - ' + str(info[2][1]) + '   ' \
                   + str(info[2][2]) + '\n' + \
                   '       \\' + '\n' + \
                   '        ' + str(info[3][0])
        elif self.length == 2:
            return start + '   ' + str(info[1][3]) + '\n' + \
                   '    / \\ / \\ /' + '\n' + \
                   ' - '.join([str(info[2][0]), str(info[2][1]),
                               str(info[2][2]), str(info[2][3])]) + '\n' + \
                   '    \\ / \\ / \\' + '\n' + \
                   '  ' + ' - '.join([str(info[3][0]), str(info[3][1]),
                                      str(info[3][2])]) \
                   + '   ' + str(info[3][3]) + '\n' + \
                   '      \\   \\' + '\n' + '      ' + str(info[4][0]) + \
                   '   ' + str(info[4][1])

        elif self.length == 3:
            start = '        ' + str(info[0][0]) +\
                    '   ' + str(info[0][1]) + '\n' + \
                    '       /   /' + '\n' + \
                '   ' + str(info[1][0]) + ' - ' + str(info[1][1]) + \
                    ' - ' + str(info[1][2])
            return start + '   ' + str(info[1][3]) + '\n' \
                   + '     / \\ / \\ /' + '\n' + \
                   ' ' + ' - '.join([str(info[2][0]),
                                     str(info[2][1]), str(info[2][2]),
                                     str(info[2][3])]) + '   ' + \
                   str(info[2][4]) + '\n' \
                   + '     / \\ / \\ / \\ /' + '\n' \
                   + ' - '.join([str(info[3][0]), str(info[3][1]),
                                 str(info[3][2]),
                                 str(info[3][3]), str(info[3][4])]) + '\n' \
                   + '     \\ / \\ / \\ / \\' + '\n'\
                   + '  ' + ' - '.join([str(info[4][0]), str(info[4][1]),
                                        str(info[4][2]),
                                        str(info[4][3])]) + '\n'\
                   + '      \\   \\   \\' + '\n' \
                   + '       ' + '    '.join([str(info[5][0]), str(info[5][1]),
                                              str(info[5][2])])
        elif self.length == 4:
            begin = '          ' + str(info[0][0]) + '   ' + str(info[0][1])\
                    + '\n'\
                    + '         /   /' + '\n'\
                    + '    ' + ' - '.join([str(info[1][0]), str(info[1][1]),
                                           str(info[1][2])]) + '   ' \
                    + str(info[1][3]) + '\n' + '       / \\ / \\ /' + '\n'\
                    + ' ' + ' - '.join([str(info[2][0]), str(info[2][1]),
                                        str(info[2][2]),
                                        str(info[2][3])]) + '   ' \
                    + str(info[2][4]) + '\n' + \
                    '     / \\ / \\ / \\ /' + '\n'
            return begin + ' - '.join([str(info[3][0]), str(info[3][1]),
                                       str(info[3][2]),
                                       str(info[3][3]), str(info[3][4])])\
                   + '   ' + str(info[3][5]) + '\n' \
                   + '  / \\ / \\ / \\ / \\ /' + '\n' \
                   + ' - '.join([str(info[4][0]), str(info[4][1]),
                                 str(info[4][2]), str(info[4][3]),
                                 str(info[4][4]), str(info[4][5])])\
                   + '\n' + '  \\ / \\ / \\ / \\ / \\' + '\n' \
                   + ' - '.join([str(info[5][0]), str(info[5][1]),
                                 str(info[5][2]), str(info[5][3]),
                                 str(info[5][4])]) + '   ' \
                   + str(info[5][5]) + '\n' \
                   + '    \\   \\   \\   \\' + '\n' \
                   + '     ' + '   '.join([str(info[6][0]), str(info[6][1]),
                                           str(info[6][2]), str(info[6][3])])
        elif self.length == 5:
            begin = '              ' + str(info[0][0]) + '   ' \
                    + str(info[0][1]) + '\n'\
                    + '             /   /' + '\n'\
                    + '        ' + ' - '.join([str(info[1][0]), str(info[1][1]),
                                               str(info[1][2])]) + '   ' \
                    + str(info[1][3]) + '\n' + '           / \\ / \\ /' + '\n'\
                    + '     ' + ' - '.join([str(info[2][0]),
                                            str(info[2][1]), str(info[2][2]),
                                            str(info[2][3])]) + '   ' \
                    + str(info[2][4]) + '\n' +\
                    '         / \\ / \\ / \\ /' + '\n' \
                        '    ' + ' - '.join([str(info[3][0]),
                                             str(info[3][1]), str(info[3][2]),
                                             str(info[3][3]), str(info[3][4])])\
                    + '   ' + str(info[3][5]) + '\n' \
                   + '       / \\ / \\ / \\ / \\ /' + '\n'
            return begin + '  ' + ' - '.join([str(info[4][0]), str(info[4][1]),
                                              str(info[4][2]), str(info[4][3]),
                                              str(info[4][4]),
                                              str(info[4][5])]) + \
                   '   ' + str(info[4][6]) \
                       + '\n' + '    / \\ / \\ / \\ / \\ / \\ /' + '\n' \
                   + ' - '.join([str(info[5][0]), str(info[5][1]),
                                 str(info[5][2]), str(info[5][3]),
                                 str(info[5][4]), str(info[5][5]),
                                 str(info[5][6])]) + '\n' + \
                       '    \\ / \\ / \\ / \\ / \\ / \\' + '\n' + \
                       ' - '.join([str(info[6][0]), str(info[6][1]),
                                   str(info[6][2]), str(info[6][3]),
                                   str(info[6][4]), str(info[6][5])]) \
                   + '   ' + str(info[6][6]) + '\n' \
                       + '    \\   \\   \\   \\   \\' + '\n' + \
                       '     ' + '   '.join([str(info[7][0]),
                                             str(info[7][1]),
                                             str(info[7][2]),
                                             str(info[7][3]), str(info[7][4])])

    def get_current_player_name(self) -> str:
        """
        Return which player is playing right now.

        >>> s = StonehengeState(True, 4)
        >>> s.get_current_player_name()
        'p1'
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def get_possible_moves(self) -> list:
        """
        Return all the letters of position that can claimed.

        >>> s = StonehengeState(True, 3)
        >>> s.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

        """
        status = False
        if self.get_current_player_name() == 'p1':
            status = True
        n = 0
        s = StonehengeState(status, self.length)
        for li in s.info:
            for ele in li:
                if ele == '@':
                    n += 1
        n1 = 0
        n2 = 0
        i = 1
        for ele in self.info[0]:
            if ele == '1':
                n1 += 1
            elif ele == '2':
                n2 += 1
        while i != self.length + 2:
            if self.info[i][0] == '1':
                n1 += 1
            if self.info[i][0] == '2':
                n2 += 1
            if self.info[i][-1] == '1' and i != self.length:
                n1 += 1
            if self.info[i][-1] == '2' and i != self.length:
                n2 += 1
            i += 1
        for ele in self.info[-1]:
            if ele == '1':
                n1 += 1
            elif ele == '2':
                n2 += 1
        if n1 >= 1 / 2 * n or n2 >= 1 / 2 * n:
            # return True
        # if self.is_over:
            return []
        # else:
        moves = []
        for l in self.info:
            for letter in l:
                if letter.isalpha():
                    moves.append(letter)
        return moves

    def make_move(self, move: str) -> 'StonehengeState':
        """
        Return the state after move has been applied.

        >>> s = StonehengeState(True, 1)
        >>> s2 = s.make_move('C')
        >>> s.info
        [['@', '@'], ['@', 'A', 'B'], ['@', 'C', '@'], ['@']]
        >>> s2.info
        [['@', '1'], ['@', 'A', 'B'], ['1', '1', '@'], ['1']]
        """

        new = copy.deepcopy(self.info)
        le = copy.deepcopy(self.length)
        # change letter
        i = 1
        while i != le + 2:
            j = 1
            while j != len(new[i]):
                if new[i][j] == move:
                    new[i][j] = self.get_current_player_name()[1]
                j += 1
            i += 1
        # change '@' in row
        i = 1
        while i != le + 2:
            n1, n2 = 0, 0
            j = 1
            # for item in new[i]:
            while j != (len(new[i]) - 1):
                if new[i][j] == '1':
                    n1 += 1
                elif new[i][j] == '2':
                    n2 += 1
                j += 1
            if i == le:
                if new[i][-1] == '1':
                    n1 += 1
                elif new[i][-1] == '2':
                    n2 += 1
                if n1 >= (len(new[i]) - 1) / 2 and new[i][0] == '@':
                    new[i][0] = '1'
                elif n2 >= (len(new[i]) - 1) / 2 and new[i][0] == '@':
                    new[i][0] = '2'
            if i != le:
                if n1 >= (len(new[i]) - 2) / 2 and new[i][0] == '@':
                    new[i][0] = '1'
                elif n2 >= (len(new[i]) - 2) / 2 and new[i][0] == '@':
                    new[i][0] = '2'
            i += 1
        # change '@' in '/'

        n1, n2 = 0, 0
        m1, m2 = 0, 0
        p1, p2, q1, q2, r1, r2, s1, s2 = 0, 0, 0, 0, 0, 0, 0, 0
        i = 1
        while i != le + 1:
            if new[i][1] == '1':
                n1 += 1
            if new[i][1] == '2':
                n2 += 1
            if new[i][2] == '1':
                m1 += 1
            if new[i][2] == '2':
                m2 += 1
            if i >= 2 and new[i][3] == '1':
                p1 += 1
            if i >= 2 and new[i][3] == '2':
                p2 += 1
            if i >= 3 and new[i][4] == '1':
                q1 += 1
            if i >= 3 and new[i][4] == '2':
                q2 += 1
            if i >= 4 and new[i][5] == '1':
                r1 += 1
            if i >= 4 and new[i][5] == '2':
                r2 += 1
            if i >= 5 and new[i][6] == '1':
                s1 += 1
            if i >= 5 and new[i][6] == '2':
                s2 += 1
            i += 1
        if new[le + 1][1] == '1':
            m1 += 1
        if new[le + 1][1] == '2':
            m2 += 1
        if le >= 2 and new[le + 1][2] == '1':
            p1 += 1
        if le >= 2 and new[le + 1][2] == '2':
            p2 += 1
        if le >= 3 and new[le + 1][3] == '1':
            q1 += 1
        if le >= 3 and new[le + 1][3] == '2':
            q2 += 1
        if le >= 4 and new[le + 1][4] == '1':
            r1 += 1
        if le >= 4 and new[le + 1][4] == '2':
            r2 += 1
        if le >= 5 and new[le + 1][5] == '1':
            s1 += 1
        if le >= 4 and new[le + 1][5] == '2':
            s2 += 1
        # count if more than half
        if n1 >= le / 2 and new[0][0] == '@':
            new[0][0] = '1'
        if n2 >= le / 2 and new[0][0] == '@':
            new[0][0] = '2'
        if m1 >= 1 / 2 * (le + 1) and new[0][1] == '@':
            new[0][1] = '1'
        if m2 >= 1 / 2 * (le + 1) and new[0][1] == '@':
            new[0][1] = '2'
        if le >= 2 and p1 >= le / 2 and new[1][-1] == '@':
            new[1][-1] = '1'
        if le >= 2 and p2 >= le / 2 and new[1][-1] == '@':
            new[1][-1] = '2'
        if le >= 3 and q1 >= 1 / 2 * (le - 1) and new[2][-1] == '@':
            new[2][-1] = '1'
        if le >= 3 and q2 >= 1 / 2 * (le - 1) and new[2][-1] == '@':
            new[2][-1] = '2'
        if le >= 4 and r1 >= 1 / 2 * (le - 2) and new[3][-1] == '@':
            new[3][-1] = '1'
        if le >= 4 and r2 >= 1 / 2 * (le - 2) and new[3][-1] == '@':
            new[3][-1] = '2'
        if le >= 5 and s1 >= 1 / 2 * (le - 3) and new[4][-1] == '@':
            new[4][-1] = '1'
        if le >= 5 and s2 >= 1 / 2 * (le - 3) and new[4][-1] == '@':
            new[4][-1] = '2'
        # change '@' in '\'
        a1, a2, b1, b2, c1, c2, d1, d2, e1, e2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        f1, f2, g1, g2, h1, h2, i1, i2 = 0, 0, 0, 0, 0, 0, 0, 0
        if new[le][1] == '1':
            a1 += 1
        if new[le + 1][1] == '1':
            a1 += 1
        if new[le][1] == '2':
            a2 += 1
        if new[le + 1][1] == '2':
            a2 += 1
        if a1 >= 1:
            new[le + 2][0] = '1'
        if a2 >= 1:
            new[le + 2][0] = '2'
        i = 1
        while i != le + 1:
            if new[i][i + 1] == '1':
                b1 += 1
            elif new[i][i + 1] == '2':
                b2 += 1
            i += 1
        if b1 >= len(new[-1]) / 2:
            new[le + 1][le + 1] = '1'
        elif b2 >= len(new[-1]) / 2:
            new[le + 1][le + 1] = '2'
        if le >= 2:
            i = 1
            while i != le + 1:
                if new[i][i] == '1':
                    c1 += 1
                elif new[i][i] == '1':
                    c2 += 1
                i += 1
            if new[le + 1][le] == '1':
                c1 += 1
            if new[le + 1][le] == '2':
                c2 += 1
            if c1 >= (le + 1) / 2:
                new[le + 2][le - 1] = '1'
            if c2 >= (le + 1) / 2:
                new[le + 2][le - 1] = '2'
        if le == 3:
            for ele in [new[2][1], new[3][2], new[4][2]]:
                if ele == '1':
                    d1 += 1
                elif ele == '2':
                    d2 += 1
            if d1 >= 1.5 and new[5][1] == '@':
                new[5][1] = '1'
            if d2 >= 1.5 and new[5][1] == '@':
                new[5][1] = '2'
        if le == 4:
            for ele in [new[3][1], new[4][2], new[5][2]]:
                if ele == '1':
                    e1 += 1
                if ele == '2':
                    e2 += 1
                if e1 >= 1.5:
                    new[6][1] = '1'
                if e2 >= 1.5:
                    new[6][1] = '2'
            for ele in [new[2][1], new[3][2], new[4][3], new[5][3]]:
                if ele == '1':
                    f1 += 1
                if ele == '2':
                    f2 += 1
                if f1 >= 2:
                    new[6][2] = '1'
                if f2 >= 2:
                    new[6][2] = '2'
        if le == 5:
            for ele in [new[4][1], new[5][2], new[6][2]]:
                if ele == '1':
                    g1 += 1
                if ele == '2':
                    g2 += 1
                if g1 >= 1.5 and new[7][1] == '@':
                    new[7][1] = '1'
                if g2 >= 1.5 and new[7][1] == '@':
                    new[7][1] = '2'
            for ele in [new[3][1], new[4][2], new[5][3], new[6][3]]:
                if ele == '1':
                    h1 += 1
                if ele == '2':
                    h2 += 1
                if ele == '1':
                    f1 += 1
                if ele == '2':
                    f2 += 1
                if h1 >= 2 and new[7][2] == '@':
                    new[7][2] = '1'
                if h2 >= 2 and new[7][2] == '@':
                    new[7][2] = '2'
            for ele in [new[2][1], new[3][2], new[4][3], new[5][4], new[6][4]]:
                if ele == '1':
                    i1 += 1
                if ele == '2':
                    i2 += 1
                if i1 >= 2.5 and new[7][3] == '@':
                    new[7][3] = '1'
                if i2 >= 2.5 and new[7][3] == '@':
                    new[7][3] = '2'
        # mutate

        s = StonehengeState(not self.p1_turn, le)
        s.info = new
        # s.board = s.board.replace(move, self.get_current_player_name()[1])
        return s

    def is_valid_move(self, move: str) -> bool:
        """
        Return whether move can be applied to state.

        >>> s = StonehengeState(True, 3)
        >>> s2 = s.make_move('C')
        >>> s2.is_valid_move('C')
        False

        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return "Player: {} - board: {}".format\
            (self.get_current_player_name(), self.__str__())

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        n = 0
        for li in self.info:
            for ele in li:
                if ele == '@':
                    n += 1
        # Count the number of leylines claimed in current state.
        n1 = 0
        n2 = 0
        i = 1
        for ele in self.info[0]:
            if ele == '1':
                n1 += 1
            elif ele == '2':
                n2 += 1
        while i != self.length + 2:
            if self.info[i][0] == '1':
                n1 += 1
            if self.info[i][0] == '2':
                n2 += 1
            if self.info[i][-1] == '1' and i != self.length:
                n1 += 1
            if self.info[i][-1] == '2' and i != self.length:
                n2 += 1
            i += 1
        for ele in self.info[-1]:
            if ele == '1':
                n1 += 1
            elif ele == '2':
                n2 += 1
        if n1 >= 1 / 2 * n:
            if self.get_current_player_name() == 'p1':
                return 1
            return -1
        elif n2 >= 1 / 2 * n:
            if self.get_current_player_name() == 'p1':
                return -1
            return 1
        else:
            moves = self.get_possible_moves()
            for move in moves:
                new = self.make_move(move)
                n1 = 0
                n2 = 0
                i = 1
                for ele in new.info[0]:
                    if ele == '1':
                        n1 += 1
                    elif ele == '2':
                        n2 += 1
                while i != new.length + 2:
                    if new.info[i][0] == '1':
                        n1 += 1
                    if new.info[i][0] == '2':
                        n2 += 1
                    if new.info[i][-1] == '1' and i != new.length:
                        n1 += 1
                    if new.info[i][-1] == '2' and i != new.length:
                        n2 += 1
                    i += 1
                for ele in new.info[-1]:
                    if ele == '1':
                        n1 += 1
                    elif ele == '2':
                        n2 += 1
                if n1 >= 1 / 2 * n:
                    if new.get_current_player_name() == 'p1':
                        return -1
                    return 1
                elif n2 >= 1 / 2 * n:
                    if new.get_current_player_name() == 'p1':
                        return 1
                    return -1
        return 0



if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod()
