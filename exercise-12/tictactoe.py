Pos = tuple[int, int]
Board = dict[Pos, str]  # Only "X", "O" and "_" are valid.


def read_board_from_file(filename: str) -> Board:
    """Return a `Board` from a simple text file which contains the current
    playing field, for example, as follows:

    XOX
    OXX
    ___
    """
    with open(filename, "r") as f:
        board = dict()

        for row, line in enumerate(f):
            for col, char in enumerate(line):
                board[(row, col)] = char if char in "XO_" else "_"

    return board


def read_board_from_str(string: str) -> Board:
    """Return a `Board` from a simple string, which contains the current
    playing field in a continous form, for example, as follows:

    XOXOXX___
    """
    assert 9 == string.count("X") + string.count("O") + string.count("_")

    board = dict()
    for row in range(3):
        for col in range(3):
            board[(row, col)] = string[row * 3 + col]

    return board


def print_board(board: Board):
    for row in range(3):
        for col in range(3):
            print(board[(row, col)], end="")
        print()


def check_three_in_a_row(board: Board, player: str) -> bool:
    for row in range(3):
        if board[(row, 0)] == player and board[(row, 1)] == player and board[(row, 2)] == player:
            return True
    for col in range(3):
        if board[(0, col)] == player and board[(1, col)] == player and board[(2, col)] == player:
            return True
    if board[(0, 0)] == player and board[(1, 1)] == player and board[(2, 2)] == player:
        return True
    elif board[(0, 2)] == player and board[(1, 1)] == player and board[(2, 0)] == player:
        return True
    return False


def calculate_score(board: Board, depth: int) -> int:
    """
    Return 10 if X wins, -10 if O wins or 0 if it is a draw or not
    decideable yet.
    """

    # Check if X wins
    if check_three_in_a_row(board, "X"):
        return 10 - depth
    elif check_three_in_a_row(board, "O"):
        return depth - 10
    else:
        return 0


def simulate_move(board: Board, move: Pos, player: str) -> Board:
    """
    Simulate a move on the board.
    """

    new_board = board.copy()
    new_board[move] = player

    return new_board


def minimax(board: Board, depth: int, max_mode: bool) -> int:
    """
    Use the minimax algorithm to determine if a current game state will
    (possibly) lead to a win, a lose or a draw.
    """

    # Check if the game is over.
    score = calculate_score(board, depth)
    if score != 0:
        return score

    # Check if there are any possible moves left.
    if len(compute_possible_moves(board)) == 0:
        return 0

    if max_mode:
        best_score = -1000
        for move in compute_possible_moves(board):
            simulated_board = simulate_move(board, move, "X")
            score = minimax(simulated_board, depth + 1, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for move in compute_possible_moves(board):
            simulated_board = simulate_move(board, move, "O")
            score = minimax(simulated_board, depth + 1, True)
            best_score = min(score, best_score)
        return best_score


def compute_possible_moves(board: Board) -> list[Pos]:
    """
    Return a list of all possible moves.
    """

    possible_moves = []
    for row in range(3):
        for col in range(3):
            if board[(row, col)] == "_":
                possible_moves += [(row, col)]

    return possible_moves


def return_best_move(board: Board) -> Pos:
    """
    Return the best move for the current player.
    """

    possible_moves = compute_possible_moves(board)
    best_move = possible_moves[0]
    best_score = -1000

    for move in possible_moves:
        simulated_board = simulate_move(board, move, "X")
        score = minimax(simulated_board, 0, False)
        if score > best_score:
            best_move = move
            best_score = score

    return best_move


if __name__ == "__main__":
    board: Board = read_board_from_file("exercise-12/game.txt")
    print(return_best_move(board))
