from two_player_games.games.connect_four import ConnectFour  # or any other game
import random


game = ConnectFour()

while not game.is_finished():
    print(game.__str__())
    moves = game.get_moves()
    move = random.choice(moves)
    game.make_move(move)

print('\n' + game.__str__())

winner = game.get_winner()
if winner is None:
    print('Draw!')
else:
    print('Winner: Player ' + winner.char)