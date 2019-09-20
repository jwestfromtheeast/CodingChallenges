class Solution:
    # Another math trick (see rotate array if you have not yet)
    # Here, to rotate the array 90 degrees clockwise, reverse the array along
    # the horizontal axis, then mirror the array
    # Complexity: Time O(n^2) Space O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        xlen = len(matrix)
        ylen = len(matrix[0])
        start, end = 0, xlen - 1
        while (start < end):
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1
        for i in range(xlen):
            for j in range(i + 1, ylen):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]