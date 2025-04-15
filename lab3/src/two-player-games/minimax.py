from two_player_games.games.connect_four import ConnectFour  # or any other game
import random

class Minimax_Player():
    def __init__(self, depth, maximizingPlayer):
        self.depth = depth
        self.maximizingPlayer = maximizingPlayer

    def score(self, current_player, state):
        # a game-dependent scoring function from the perspective of the current_player
        # print(state)
        # print('score:', state.score(current_player), '\n')
        return state.score(current_player)

    def chose_random_highest(self, move_scores):
        best_moves = []
        best_score = float('-inf')
        for move, score in move_scores:
            if score > best_score:
                best_moves = []
                best_score = score
            if score >= best_score:
                best_moves.append(move)
        return random.choice(best_moves)

    def play_randomly(self, node):
        #     if depth == 0 or node.is_finished:
        #         return score(node)
        curr_player = node.get_current_player()
        moves = node.get_moves()

        move_scores = [
            (move, self.score(curr_player, node.state.make_move(move)))
            for move in moves
        ]  # note that `state.make_move()` does not change the game state

        move = self.chose_random_highest(move_scores)
        return move
    
    def minimax(self, node):
        depth = self.depth
        if depth == 0 or node.is_finished():
            return score(node)
        curr_player = node.get_current_player()
        moves = node.get_moves()

        move_scores = [
            (move, self.score(curr_player, node.state.make_move(move)))
            for move in moves
        ]  # note that `state.make_move()` does not change the game state

        move = self.chose_random_highest(move_scores)
        return move

def play_game(p1, p2):
    game = ConnectFour()
    p1_turn = True

    while not game.is_finished():
        if p1_turn:
            game.make_move(p1.minimax(game, p1))
        
        else:
            game.make_move(p2.minimax(game, p2))

        p1_turn = not p1_turn
        print(game)

    winner = game.get_winner()
    if winner is None:
        print('Draw!')
    else:
        print('Winner: Player ' + winner.char)


p1 = Minimax_Player(1)
p2 = Minimax_Player(1)
play_game(p1, p2)