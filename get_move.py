from minimax import minimax
from custom_thread import CustomThread

def thread_function(board, depth, move):
    board.push(move)
    score = minimax(board, depth - 1, -9999, 9999)
    board.pop()

    return [score, move]

def get_move(board, depth):
    best_move = None
    best_score = -9999

    threads = []
    for move in board.legal_moves:
        board_copy = board.copy()

        t = CustomThread()
        t.function = thread_function
        t.args = (board_copy, depth, move)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
        score, move = t.value

        if not board.turn:
            score *= -1

        if score >= best_score:
            best_score = score
            best_move = move     
         
    return best_move