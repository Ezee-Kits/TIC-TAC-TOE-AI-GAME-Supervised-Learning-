import pandas as pd
from itertools import product






# Generate all possible board states
# positions = [-1, 0, 1]
# all_boards = []

# # 3^9 total combinations
# for board in product(positions, repeat=9):
#     num_ai = board.count(-1)
#     num_player = board.count(1)

#     # AI first
#     if num_ai == num_player or num_ai == num_player + 1:
#         all_boards.append(board)
#     # Player first
#     elif num_player == num_ai or num_player == num_ai + 1:
#         all_boards.append(board)

# print(f"Total valid boards respecting both turn orders: {len(all_boards)}")

# # For ML: each empty space becomes its own row
# data = []
# for board in all_boards:
#     for idx, v in enumerate(board):
#         if v == 0:
#             data.append(list(board) + [idx+1])  # idx+1 because positions 1-9

# columns = [f"pos{i}" for i in range(1,10)] + ["y"]
# df = pd.DataFrame(data, columns=columns)

# # Save to CSV
# csv_path = "tic_tac_toe_all_states_both_first.csv"
# df.to_csv(csv_path, index=False)




# import pandas as pd
# from itertools import product
# from copy import deepcopy

# # All 8 possible winning line indexes
# WIN_COMBOS = [
#     [0,1,2],[3,4,5],[6,7,8],    # Rows
#     [0,3,6],[1,4,7],[2,5,8],    # Columns
#     [0,4,8],[2,4,6]             # Diagonals
# ]

# def check_winner(board):
#     """Return -1 if AI wins, 1 if player wins, 0 otherwise"""
#     for combo in WIN_COMBOS:
#         line = [board[i] for i in combo]
#         if line == [-1, -1, -1]:
#             return -1
#         elif line == [1, 1, 1]:
#             return 1
#     return 0

# positions = [-1, 0, 1]
# all_boards = []

# # Generate all logically valid boards
# for board in product(positions, repeat=9):
#     num_ai = board.count(-1)
#     num_player = board.count(1)

#     # Valid turn balance (AI or player may start)
#     if abs(num_ai - num_player) <= 1:
#         all_boards.append(board)

# data = []

# # Evaluate all possible next moves
# for board in all_boards:
#     winner = check_winner(board)
#     if winner != 0:  # Skip finished games
#         continue

#     for idx, v in enumerate(board):
#         if v == 0:  # Empty spot
#             new_board = list(deepcopy(board))
#             new_board[idx] = -1  # Assume AI plays next
#             outcome = check_winner(new_board)
            
#             if outcome == -1:
#                 score = 1   # Winning move
#             else:
#                 # Simulate player’s counter move
#                 score = 0
#                 for j in range(9):
#                     if new_board[j] == 0:
#                         reply = list(deepcopy(new_board))
#                         reply[j] = 1
#                         if check_winner(reply) == 1:
#                             score = -1   # Losing move
#                             break
#             data.append(list(board) + [idx + 1, score])

# # Create DataFrame
# columns = [f"pos{i}" for i in range(1, 10)] + ["y", "score"]
# df = pd.DataFrame(data, columns=columns)

# # Save to CSV
# csv_path = "tic_tac_toe_training_weighted.csv"
# df.to_csv(csv_path, index=False)


import pandas as pd
from itertools import product

def check_winner(board):
    """Return -1 if AI wins, 1 if Player wins, else 0"""
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if board[a] != 0 and board[a] == board[b] == board[c]:
            return board[a]
    return 0  # no winner

def score_move_on_nonterminal(board, move, player_turn):
    """
    Simulate player_turn placing at `move` and return:
      -1 if AI wins after move
       1 if Player wins after move
       0 otherwise (draw or ongoing)
    """
    temp = list(board)
    temp[move] = player_turn
    winner_after = check_winner(temp)
    if winner_after == -1:
        return -1
    elif winner_after == 1:
        return 1
    else:
        return 0

positions = [-1, 0, 1]
data = []

for board in product(positions, repeat=9):
    num_ai = board.count(-1)
    num_player = board.count(1)

    # Only valid turn orders (difference ≤ 1)
    if abs(num_ai - num_player) <= 1:
        # Determine whose turn it would be if the game is ongoing
        player_turn = -1 if num_ai <= num_player else 1

        # Check if board is already terminal
        existing_winner = check_winner(board)

        # For each empty spot, compute the score
        for idx, v in enumerate(board):
            if v == 0:
                if existing_winner != 0:
                    # Board already has a winner -> score is that winner
                    score = existing_winner
                else:
                    # Board not terminal -> simulate the move by whose turn it is
                    score = score_move_on_nonterminal(board, idx, player_turn)
                data.append(list(board) + [idx + 1, score])

# Create DataFrame
columns = [f"pos{i}" for i in range(1, 10)] + ["move", "score"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
csv_path = "DATASET/tic_tac_toe_training_weighted.csv"
df.to_csv(csv_path, index=False)

print(f"✅ Dataset saved as {csv_path} with {len(df)} rows")
print(df['score'].value_counts())

