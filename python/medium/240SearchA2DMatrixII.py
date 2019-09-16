class Solution:
    # Idea: Since size grows from left to right and bottom to top, the middle value should be in the top right
    # From there, compare the number to the target each time and adjust accordingly
    # If you are larger than the target, move left to get a smaller number
    # If you are smaller than the target, move down to get a larger number
    # Else, you found your solution
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Complexity: O(n) time (where n is max of len(matrix) & len(matrix[0])), O(1) space
        if not len(matrix) or not len(matrix[0]):
            return False
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True
        return False