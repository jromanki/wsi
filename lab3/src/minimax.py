from two_player_games.games.connect_four import ConnectFour  # or any other game
import random

class Minimax_Player():
    def __init__(self, depth, maximizingPlayer, alphabeta):
        self.depth = depth
        self.maximizingPlayer = maximizingPlayer
        self.alphabeta = alphabeta

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
    
    def minimax(self, node, parrent_node, depth, maximizingPlayer):
        if depth == 0 or node.is_finished():
            return self.score(parrent_node.get_current_player(), node)

        if maximizingPlayer:
            max_score = float('-inf')
            for move in node.get_moves():
                score = self.minimax(node.make_move(move), parrent_node, depth-1, False)
                max_score = max(max_score, score)
            return max_score

        else:
            min_score = float('inf')
            for move in node.get_moves():
                score = self.minimax(node.make_move(move), parrent_node, depth-1, True)
                min_score = min(min_score, score)
            return min_score
    
    def minimax_ab(self, node, parrent_node, depth, a, b, maximizingPlayer):
        if depth == 0 or node.is_finished():
            return self.score(parrent_node.get_current_player(), node)

        if maximizingPlayer:
            max_score = float('-inf')
            for move in node.get_moves():
                score = self.minimax_ab(node.make_move(move), node, depth-1, a, b, False)
                max_score = max(max_score, score)
                a = max(a, max_score)
                if max_score >= b:
                    break # b cutoff
            return max_score

        else:
            min_score = float('inf')
            for move in node.get_moves():
                score = self.minimax_ab(node.make_move(move), node, depth-1, a, b, True)
                min_score = min(min_score, score)
                b = min(b, min_score)
                if min_score <= a:
                    break # a cutoff
            return min_score

    def move_minimax(self, node):
        depth = self.depth
        moves = node.get_moves()

        if self.alphabeta:
            a, b = float('-inf'), float('inf')
            move_scores = [
                (move, self.minimax_ab(node.state.make_move(move), node, depth, a, b, self.maximizingPlayer))
                for move in moves
            ]  # note that `state.make_move()` does not change the game state

        else:
            move_scores = [
                (move, self.minimax(node.state.make_move(move), node, depth, self.maximizingPlayer))
                for move in moves
            ]  # note that `state.make_move()` does not change the game state

        move = self.chose_random_highest(move_scores)
        return move
    
    def move_randomly(self, node):
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

def play_game(depth1, depth2, alphabeta):
    game = ConnectFour()
    p1 = Minimax_Player(depth1, True, alphabeta)
    p2 = Minimax_Player(depth2, False, alphabeta)
    p1_turn = True

    while not game.is_finished():
        if p1_turn:
            game.make_move(p1.move_minimax(game))
        
        else:
            game.make_move(p2.move_minimax(game))

        p1_turn = not p1_turn
        # print(game)

    winner = game.get_winner()
    # if winner is None:
    #     print('Draw!')
    # else:
    #     print('Winner: Player ' + winner.char)
    if winner is None:
        return 0
    else:
        if winner.char == '1':
            return 1
        elif winner.char == '2':
            return 0

play_game(1, 5, True)