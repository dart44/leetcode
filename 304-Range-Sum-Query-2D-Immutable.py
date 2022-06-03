class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (COLS + 1) for r in range (ROWS + 1)]
        
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sum_matrix[r][c + 1]
                self.sum_matrix[r + 1][c + 1] = prefix + above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2, = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        bottom_right = self.sum_matrix[r2][c2]
        above = self.sum_matrix[r1 - 1][c2]
        left = self.sum_matrix[r2][c1 - 1]
        top_left = self.sum_matrix[r1 - 1][c1 - 1]
        
        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# Test
def main():
    test = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(f'{test.sumRegion(2, 1, 4, 3)}')
    print(f'{test.sumRegion(1, 1, 2, 2)}')
    print(f'{test.sumRegion(1, 2, 2, 4)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()