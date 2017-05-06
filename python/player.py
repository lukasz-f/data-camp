class Player:
    moves = ['papier', 'nozyce', 'kamien']

    def __init__(self, score=0, name='', can_finish_game=False):
        self.score = score
        self.name = name
        self.can_finish_game = can_finish_game

    def get_move(self):
        pass

    def set_name(self):
        pass

    def check_exit(self):
        pass


class ComputerPlayer(Player):
    def set_name(self):
        self.name = 'Computer'

    def check_exit(self):
        return False


class HumanPlayer(Player):
    def __init__(self):
        super().__init__(can_finish_game=True)

    def set_name(self):
        self.name = input('Podaj imie: ')

    def check_exit(self):
        while True:
            exit = input('Czy chcesz zakonczyc? (T/N):')
            if exit.upper() in ['T', 'N']:
                return exit.upper() == 'T'


humanPlayer = HumanPlayer()
humanPlayer.set_name()
print('Human score:', humanPlayer.score)
print('Human can finish game:', humanPlayer.can_finish_game)
humanPlayer.check_exit()
