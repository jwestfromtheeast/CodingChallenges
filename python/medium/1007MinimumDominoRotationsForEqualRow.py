class Solution:
    # Complexity: Time O(n), Space O(1)
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A) != len(B):
            return -1
        
        a_count = [0 for i in range(7)]
        b_count = [0 for i in range(7)]
        same_count = [0 for i in range(7)]
        for i in range(len(A)):
            a_count[A[i]] += 1
            b_count[B[i]] += 1
            if A[i] == B[i]:
                same_count[A[i]] += 1
        
        min_rotations = float('inf')
        for i in range(1, 7):
            if a_count[i] + b_count[i] - same_count[i] >= len(A):
                curr_rotations = min(a_count[i], b_count[i]) - same_count[i]
                min_rotations = min(curr_rotations, min_rotations)
        return min_rotations if min_rotations != float('inf') else -1