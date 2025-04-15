from two_player_games.games.connect_four import ConnectFour  # or any other game
import random


def score(current_player, state):
    # a game-dependent scoring function from the perspective of the current_player
    print(state)

game = ConnectFour()

while not game.is_finished():
    moves = game.get_moves()

    move = moves[int(input())]
    print(game.state.make_move(move))
    game.make_move(move)
    print('score:', game.state.score(), '\n')

#     move_scores = [
#         (move, score(game.get_current_player(), game.state.make_move(move)))
#         for move in moves
#     ]  # note that `state.make_move()` does not change the game state

#     move = max(move_scores, key=lambda ms: ms[1])[0]
    # game.make_move(move)

winner = game.get_winner()
if winner is None:
    print('Draw!')
else:
    print('Winner: Player ' + winner.char)