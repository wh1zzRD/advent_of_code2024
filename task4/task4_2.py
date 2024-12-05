def is_in_matrix(matrix, row, col):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    # Check if the coordinates are within bounds
    return 0 <= row < num_rows and 0 <= col < num_cols


def check_letter(matrix, row, col, letter, check_matrix):
    if not is_in_matrix(matrix, row, col):
        return False
    if matrix[row][col] == "A" and check_matrix[row][col] == 2:
        return False
    if matrix[row][col] == letter:
        return True
    return False


def check_word(matrix, row, col, direction, check_matrix):
    letters = ["M", "A", "S"]
    delta_row, delta_col = direction[0], direction[1]
    found = True
    for i in range(3):
        if not check_letter(matrix, row + i*delta_row, col + i*delta_col, letters[i], check_matrix):
            found = False
            break
    if found and ((check_letter(matrix, row, col + 2*delta_col, "S", check_matrix) and check_letter(matrix, row + 2*delta_row, col, "M", check_matrix)) or (check_letter(matrix, row, col + 2*delta_col, "M", check_matrix) and check_letter(matrix, row + 2*delta_row, col, "S", check_matrix))):
        check_matrix[row + delta_row][col + delta_col] = 2
        return True

    if not found:
        found = True
        for i in range(3):
            if not check_letter(matrix, row + i*delta_row, col + i*delta_col, letters[i], check_matrix):
                return False

    if found and ((check_letter(matrix, row, col + 2*delta_col, "S", check_matrix) and check_letter(matrix, row + 2*delta_row, col, "M", check_matrix)) or (check_letter(matrix, row, col + 2*delta_col, "M", check_matrix) and check_letter(matrix, row + 2*delta_row, col, "S", check_matrix))):

        check_matrix[row + delta_row][col + delta_col] = 2
        return True


def main():
    matrix = []
    with open("task4_input.txt", "r") as file:
        for line in file:
            row = [char for char in line.strip() if char.isalpha()]
            matrix.append(row)

    directions = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    result = 0

    check_matrix = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "A":
                check_matrix[i].append(1)
            else:
                check_matrix[i].append(0)

    for row in check_matrix:
        print(row)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for direction in directions:
                if check_word(matrix, i, j, direction, check_matrix):
                    result += 1

    print(result)


if __name__ == '__main__':
    main()
