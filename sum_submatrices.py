# https://www.geeksforgeeks.org/sum-of-all-submatrices-of-a-given-matrix/


def matrixSum(arr):
    n = len(arr)
    sum = 0

    for i in range(n):
        for j in range(n):
            top_left = (i + 1) * (j + 1)
            bottom_right = (n - i) * (n - j)
            sum += top_left * bottom_right * arr[i][j]

    return sum


if __name__ == "__main__":
    arr = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(matrixSum(arr))
