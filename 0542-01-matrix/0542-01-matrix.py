class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]: 
        row_length = len(mat)
        col_length = len(mat[0])

        result = [[float('inf') for _ in range(col_length)] for _ in range(row_length)]


        for row in range(row_length):
            for col in range(col_length):
                if mat[row][col] == 0:
                    result[row][col] = 0
                else:
                    if row > 0:
                        result[row][col] = min(result[row][col], result[row - 1][col] + 1)
                    if col > 0:
                        result[row][col] = min(result[row][col], result[row][col - 1] + 1)

        for row in range(row_length - 1, - 1, - 1):
            for col in range(col_length - 1, - 1, - 1):
                if row < row_length -1:
                    result[row][col] = min(result[row][col], result[row + 1][col] + 1)
                if col < col_length - 1:
                    result[row][col] = min(result[row][col], result[row][col + 1] + 1)

        return result