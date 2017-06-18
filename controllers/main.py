from models.board import Board
from models.ship import Ship
from views.console import Console


class Main:
    """The main controller.

    Sets up other controllers, models, and views.
    Starts and controls the game
    """

    def __init__(self):
        self.board = Board(5, 5)

    def main(self):
        print("Let's play Battleship!")

        ship = Ship(self.board.random_row(), self.board.random_col())
        self.board.place_ship(ship.row, ship.col)

        Console.print_board(self.board.board)

        for turn in range(4):
            guess_row = int(input("Guess Row:")) - 1
            guess_col = int(input("Guess Col:")) - 1

            shoot = self.board.shoot_spot(guess_row, guess_col)
            print(shoot['message'])

            if shoot['hit']:
                if len(self.board.ships) == 0:
                    print('Congratulations! You have sunk every ship')
                    break

            print("Turn", turn + 1)
            Console.print_board(self.board.board)
            if turn == 3:
                print("Game Over")
