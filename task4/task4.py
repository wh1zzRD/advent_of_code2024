import re


def is_in_matrix(matrix, row, col):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    # Check if the coordinates are within bounds
    return 0 <= row < num_rows and 0 <= col < num_cols


def check_letter(matrix, row, col, letter):
    if is_in_matrix(matrix, row, col) and matrix[row][col] == letter:
        return True
    return False


def check_word(matrix, row, col, direction):
    letters = ["X", "M", "A", "S"]
    delta_row, delta_col = direction[0], direction[1]
    for i in range(4):
        if not check_letter(matrix, row + i*delta_row, col + i*delta_col, letters[i]):
            return False

    return True


def main():
    matrix = []
    with open("task4_input.txt", "r") as file:
        for line in file:
            # Remove whitespace (like newline characters) and split into letters
            row = [char for char in line.strip() if char.isalpha()]  # Keep only letters
            matrix.append(row)

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    result = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for direction in directions:
                if check_word(matrix, i, j, direction):
                    result += 1

    print(result)


if __name__ == '__main__':
    main()
