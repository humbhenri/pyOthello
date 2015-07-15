# Minimax module
# Implements a generic minimax with alpha-beta
# prunning algorithm for games like chess or reversi.
# Thu Feb 18 21:54:38 Humberto Pinheiro

INFINITY = 100000


class Minimax(object):

    def __init__(self, heuristic_eval):
        """ Create a new minimax object
        player - current player's color
        opponent - opponent's color
        """
        self.heuristic_eval = heuristic_eval

    # error: always return the same board in same cases
    def minimax(self, board, parentBoard, depth, player, opponent,
                alfa=-INFINITY, beta=INFINITY):
        bestChild = board
        if depth == 0:
            return (self.heuristic_eval(parentBoard, board, depth,
                                        player, opponent), board)
        for child in board.next_states(player):
            score, newChild = self.minimax(
                child, board, depth - 1, opponent, player, -beta, -alfa)
            score = -score
            if score > alfa:
                alfa = score
                bestChild = child
            if beta <= alfa:
                break
        return (self.heuristic_eval(board, board, depth, player,
                                    opponent), bestChild)
