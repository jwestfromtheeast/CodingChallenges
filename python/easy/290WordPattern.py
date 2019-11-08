class Solution:
    # Idea: Store maps that cross-reference one another (one converts the pattern string to actual string, and vice versa)
    # Complexity: Time O(n) Space O(n)
    def wordPattern(self, pattern: str, str: str) -> bool:
        patstr = {}
        strpat = {}
        split = str.split(' ')
        if len(pattern) != len(split):
            return False
        for i in range(len(split)):
            if pattern[i] in patstr:
                if patstr[pattern[i]] != split[i]:
                    return False
            else:
                if split[i] in strpat:
                    if strpat[split[i]] != pattern[i]:
                        return False
                else:
                    patstr[pattern[i]] = split[i]
                    strpat[split[i]] = pattern[i]
        return True