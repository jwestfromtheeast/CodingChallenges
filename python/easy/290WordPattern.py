class Solution:
    # Idea: Have a map that records which pattern corresponds to which string
    # Then, have a set to record strings visited so far, in case you have not seen a pattern but have seen a string (would be False)
    # Complexity: Time O(n) Space O(n)
    def wordPattern(self, pattern: str, str: str) -> bool:
        patToStr = {}
        strVisited = set()
        split = str.split(' ')
        if len(pattern) != len(split):
            return False
        for i in range(len(split)):
            if pattern[i] in patToStr:
                if patToStr[pattern[i]] != split[i]:
                    return False
            else:
                if split[i] in strVisited:
                    return False
                else:
                    patToStr[pattern[i]] = split[i]
                    strVisited.add(split[i])
        return True