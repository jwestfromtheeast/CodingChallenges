import math
from heapq import heappush, heappop, heapreplace, heapify
class Solution:
    # Complexity: Time O(nlogn), Space O(n)
    def kClosestSort(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]
    
    # Put into a min heap instead of sorting
    def kClosestMin(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = [(math.sqrt(x[0] * x[0] + x[1] * x[1]), x) for x in points]
        heapify(dist)
        return [heappop(dist)[1] for x in range(K)]
    
    # Put into a max heap instead of sorting, and pop the biggest if the size becomes greater than K
    # This improves time to O(nlogk) and space to O(k)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = []
        heapify(dist)
        for point in points:
            heappush(dist, [-1 * math.sqrt(point[0] ** 2 + point[1] ** 2), point])
            if len(dist) > K:
                heappop(dist)
        return [x[1] for x in dist]