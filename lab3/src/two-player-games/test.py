from two_player_games.games.connect_four import ConnectFour  # or any other game
import random


def score(current_player, state):
    # a game-dependent scoring function from the perspective of the current_player
    print(state)
    print('score:', state.score(current_player), '\n')
    return state.score(current_player)

def chose_random_highest(move_scores):
    best_moves = []
    best_score = float('-inf')
    for move, score in move_scores:
        if score > best_score:
            best_moves = []
            best_score = score
        if score >= best_score:
            best_moves.append(move)
    return random.choice(best_moves)

game = ConnectFour()

while not game.is_finished():
    moves = game.get_moves()

    move_scores = [
        (move, score(game.get_current_player(), game.state.make_move(move)))
        for move in moves
    ]  # note that `state.make_move()` does not change the game state

    move = chose_random_highest(move_scores)
    game.make_move(move)

winner = game.get_winner()
if winner is None:
    print('Draw!')
else:
    print('Winner: Player ' + winner.char)