import random


def initialize_board():
    """
    Initializes a Tic Tac Toe board with empty spaces.

    Returns:
    - board (list): A 3x3 grid representing the Tic Tac Toe board.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board


def make_move(board, player, row, column):
    """
    Makes a move on the Tic Tac Toe board for the specified player.

    Parameters:
    - board (list): The Tic Tac Toe board.
    - player (str): The player making the move ('O' or 'X').
    - row (int): The row where the move is made.
    - column (int): The column where the move is made.

    Returns:
    - success (bool): True if the move is successful, False if the chosen position is already occupied.
    """
    if board[row][column] == ' ':
        board[row][column] = player
        return True
    else:
        return False


def check_winner(board):
    """
    Checks if there is a winner on the Tic Tac Toe board.

    Parameters:
    - board (list): The Tic Tac Toe board.

    Returns:
    - winner (bool): True if there is a winner, False otherwise.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def generate_random_board(num_moves):
    """
    Generates a random Tic Tac Toe board after a specified number of moves.

    Parameters:
    - num_moves (int): The number of moves made on the board.

    Returns:
    - board (list): A 3x3 grid representing the generated Tic Tac Toe board.
    """
    players = ['O', 'X']

    while True:
        board = initialize_board()
        moves_made = 0

        while moves_made < num_moves:
            current_player = players[moves_made % 2]
            row = random.randint(0, 2)
            column = random.randint(0, 2)

            if make_move(board, current_player, row, column):
                moves_made += 1

        if not check_winner(board):
            return board


def display_board(board):
    """
    Displays the Tic Tac Toe board.

    Parameters:
    - board (list): The Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def complete_lists_with_dictionary(lists, dictionary):
    """
    Completes lists with characters from a dictionary.

    Parameters:
    - lists (list): A list of lists to be completed.
    - dictionary (dict): A dictionary where keys are binary strings and values are probabilities.

    Returns:
    - result (list): A list of lists with characters filled in from the dictionary.
    """
    result = []

    for key, value in dictionary.items():
        # Create a copy of the original list
        new_list = [list(row) for row in lists]

        # Convert the binary value of the key into a list of characters 'O' and 'X'
        characters = ['O' if bit == '0' else 'X' for bit in key]

        # Fill in the empty spaces in the new list with the corresponding characters
        index = 0
        for i in range(len(new_list)):
            for j in range(len(new_list[i])):
                if new_list[i][j] == ' ':
                    new_list[i][j] = characters[index]
                    index += 1

        result.append(new_list)

    return result


def filter_values_above_average(dictionary):
    """
    Filters values above the average from a dictionary.

    Parameters:
    - dictionary (dict): A dictionary where keys are binary strings and values are probabilities.

    Returns:
    - filtered_dictionary (dict): A dictionary with values above the average.
    """
    values = list(dictionary.values())
    average = sum(values) / len(values)

    # Calculate the difference between the maximum and minimum values
    max_min_difference = max(values) - min(values)

    # Check if the difference is small compared to the average
    if max_min_difference < 0.1 * average:
        return dictionary

    # Filter values above the average
    filtered_dictionary = {key: value for key,
                           value in dictionary.items() if value > average}
    return filtered_dictionary


if __name__ == '__main__':
    # Example of usage
    num_moves = 5
    random_board = generate_random_board(num_moves)
    print(random_board)
    print('Board:')
    display_board(random_board)
