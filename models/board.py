from random import randint


class Board:
    """The game board"""

    def __init__(self, height: int, width: int):
        """Setup the game board.
        Create a two dimensional list that represents the game board.

        :param height: Height of the board
        :param width: Width of the board
        """
        self.height = height
        self.width = width

        self.board = []
        for x in range(self.height):
            self.board.append(["O"] * self.width)

        self.ships = []

    def place_ship(self, row: int, col: int) -> bool:
        """ Places a ship at the given coordinates. If a ship is
        already placed at the coordinates given, return false

        :param row: Row of the ship
        :param col: Col of the ship

        :return: bool: True if a ship is placed, false otherwise
        """
        for ship in self.ships:
            if ship['row'] == row and ship['col'] == col:
                return False

        self.ships.append({'row': row, 'col': col})
        return True

    def shoot_spot(self, row: int, col: int) -> dict:
        """
        Shoots the given spot in the board

        :param row: The row to shoot
        :param col: The col to shoot

        :return: A dictionary containing a message and a bool.
                The bool is true if you hit, false if you miss
        """
        for ship in self.ships:
            if ship['row'] == row and ship['col'] == col:
                self.ships.remove(ship)
                self.board[row][col] = "S"
                return {'message': 'Battleship sunk!', 'hit': True}

        if (row < 0 or row > 4) or (col < 0 or col > 4):
            return {'message': "Oops, that's not even in the ocean.", 'hit': False}
        elif self.board[row][col] == "X" or self.board[row][col] == "S":
            return {'message': "You guessed that one already.", 'hit': False}
        else:
            self.board[row][col] = "X"
            return {'message': "You missed!", 'hit': False}

    def random_row(self) -> int:
        return randint(0, self.width - 1)

    def random_col(self) -> int:
        return randint(0, self.height - 1)