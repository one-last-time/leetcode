class Solution:
    def valid_cell(self, r, c, row, col, vis):
        if r < 0 or r >= row or c < 0 or c >= col:
            return False
        if vis[r][c]:
            return False
        return True

    def traverse(self, cur_r, cur_c, cur_direction, directions, vis, grid, max_row, max_col):
        res = [grid[cur_r][cur_c]]
        vis[cur_r][cur_c] = 1
        next_r = cur_r + directions[cur_direction][0]
        next_c = cur_c + directions[cur_direction][1]
        if not self.valid_cell(next_r, next_c, max_row, max_col, vis):
            cur_direction += 1
            cur_direction %= 4
            next_r = cur_r + directions[cur_direction][0]
            next_c = cur_c + directions[cur_direction][1]
            if not self.valid_cell(next_r, next_c, max_row, max_col, vis):
                return res
        return res + self.traverse(next_r, next_c, cur_direction, directions, vis, grid, max_row, max_col)

    def spiralOrder(self, matrix):
        import copy
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_row = len(matrix)
        max_col = len(matrix[0])
        visrow = [0] * max_col
        vis = [copy.deepcopy(visrow) for i in range(max_row)]
        res = self.traverse(0, 0, 0, directions, vis, matrix, max_row, max_col)
        return res

res = Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)