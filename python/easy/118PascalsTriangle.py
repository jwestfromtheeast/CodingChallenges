class Solution:
    # Complexity: Time O(n^2), Space O(n^2), where n = numRows
    # See above code below, this is simply more succinct but equally efficient
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        pascal = [[1 for j in range(i + 1)] for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal

    # Perhaps slightly more intuitive, build the next row based on the previous one, then append it
    def generate2(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        # Base cases
        pascal = [[1], [1, 1]]
        # Fill in remaining cases from previous one
        for i in range(2, numRows):
            nextRow = [1]
            for j in range(1, i):
                nextRow.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            nextRow.append(1)
            pascal.append(nextRow)
        return pascal