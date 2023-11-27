import numpy as np

def count_consecutive_ones(array, val):
    rows, cols = array.shape
    consecutive_ones_diagonals = [0] * 24
    consecutive_ones_rows = [0] * rows
    consecutive_ones_cols = [0] * cols

    # Function to count consecutive ones in a 1D array
    def count_consecutive_ones_1d(arr):
        count = 0
        max_count = 0
        for elem in arr:
            if elem == val:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max(max_count - 3, 0)

    # Iterate through main diagonals
    i = 0
    for d in range(-rows + 1, cols):
        diagonal = np.diagonal(array, offset=d)
        consecutive_ones_diagonals[i] = count_consecutive_ones_1d(diagonal)
        i += 1

    # Iterate through anti-diagonals
    for d in range(-rows + 1, cols):
        diagonal = np.diagonal(np.fliplr(array), offset=d)
        consecutive_ones_diagonals[i] = count_consecutive_ones_1d(diagonal)
        i += 1

    # Count consecutive ones in rows
    for i in range(rows):
        consecutive_ones_rows[i] = count_consecutive_ones_1d(array[i, :])

    # Count consecutive ones in columns
    for j in range(cols):
        consecutive_ones_cols[j] = count_consecutive_ones_1d(array[:, j])

    score = sum(consecutive_ones_cols) + sum(consecutive_ones_rows) + sum(consecutive_ones_diagonals)
    return score, consecutive_ones_diagonals, consecutive_ones_rows, consecutive_ones_cols

# Example usage
array_2d = np.array([['1', '1', '1', '1', '1', '1', '1'],
                     ['1', '1', '1', '1', '1', '1', '1'],
                     ['1', '1', '1', '1', '1', '1', '1'],
                     ['1', '1', '1', '1', '1', '1', '1'],
                     ['1', '1', '1', '1', '1', '1', '1'],
                     ['1', '1', '1', '1', '1', '1', '1']])

score, consecutive_ones_diagonals, consecutive_ones_rows, consecutive_ones_cols = count_consecutive_ones(array_2d, '1')

print ("score:", score)
print("Consecutive ones in diagonals:", consecutive_ones_diagonals)
print("Consecutive ones in rows:", consecutive_ones_rows)
print("Consecutive ones in columns:", consecutive_ones_cols)
