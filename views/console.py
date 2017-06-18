class Console:
    """"Displays the game in a console"""

    @staticmethod
    def print_board(board: list):
        """Print out a two dimensional list that represents the game board

        :param board The two dimensional list representing the board
        """
        for row in board:
            print(" ".join(row))
