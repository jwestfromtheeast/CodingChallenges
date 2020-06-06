class Solution:
    # Complexity: Time O(n^2), Space O(n)
    # Time complexity here is limited by the for loop, because the list insert operation is O(n) itself, plus the loop makes it O(n^2)
    # You could probably use some other intermediate hashing structure to get constant time inserts, and have the sort be the limiter, reduce to O(nlogn)
    # Logic: Greedy approach, sort and you can guarentee things happen in the order you want them to.
    # Here, you know the shortest person represented by (h, k) MUST be at position k, as everyone else is greater than or equal to them in height
    # Then, the second shortest person must follow the same guideline, but is one lower priority than the shortest person, and so on.
    # To achieve this, we sort the list into reverse order, so the shortest person gets inserted last into the appropriate spot.
    # The tallest person will only have to worry about people of equal height, so we secondary sort by k, or position.
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        out = []
        for person in people:
            out.insert(person[1], [person[0], person[1]])
        return out
