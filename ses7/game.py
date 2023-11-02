class Bird:
    def __init__(self, position=(2, 2)):
        self.position = position
        self.direction = (0, 1)  # Initial direction is moving right

    def move_forward(self):
        self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])

    def turn_left(self):
        if self.direction == (0, 1):
            self.direction = (-1, 0)
        elif self.direction == (-1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (1, 0)
        else:
            self.direction = (0, 1)

    def turn_right(self):
        if self.direction == (0, 1):
            self.direction = (1, 0)
        elif self.direction == (1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (-1, 0)
        else:
            self.direction = (0, 1)

    def lose(self):
        print("Bird lost!")

    def win(self):
        print("Bird won!")

class Pig:
    def __init__(self, position=(7, 5)):
        self.position = position

    def lose(self):
        print("Pig lost!")

    def win(self):
        print("Pig won!")

class Board:
    def __init__(self):
        self.bird = Bird()
        self.pig = Pig()
        self.board_size = 10

    def display(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                if (i, j) == self.bird.position:
                    row.append('B')
                elif (i, j) == self.pig.position:
                    row.append('P')
                else:
                    row.append('*')
            print(' '.join(row))

class Workspace:
    @staticmethod
    def display_instructions():
        print("""
        Commands:
        M - Move Forward
        L - Turn Left
        R - Turn Right
        Q - Quit
        """)

    @staticmethod
    def get_commands():
        commands = input("Enter your commands: ")
        return [command.upper() for command in commands]

class Game:
    def __init__(self):
        self.board = Board()
        self.workspace = Workspace()

    def run(self):
        self.workspace.display_instructions()
        while True:
            self.board.display()
            commands = self.workspace.get_commands()
            
            for command in commands:
                if command == 'M':
                    self.board.bird.move_forward()
                elif command == 'L':
                    self.board.bird.turn_left()
                elif command == 'R':
                    self.board.bird.turn_right()
                elif command == 'Q':
                    return

            if self.board.bird.position == self.board.pig.position:
                self.board.bird.win()
                self.board.pig.lose()
                return
            if not (0 <= self.board.bird.position[0] < 10) or not (0 <= self.board.bird.position[1] < 10):
                self.board.bird.lose()
                return

if __name__ == "__main__":
    game = Game()
    game.run()
