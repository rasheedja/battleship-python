class Ship:
    """A ship"""

    def __init__(self, row: int, col: int):
        """
        Creates a ship and places it at the given coordinates

        :param row: The row where the ship should be placed
        :param col: The col where the ship should be placed
        """
        self.row = row
        self.col = col
