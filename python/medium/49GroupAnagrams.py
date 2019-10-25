class Solution:
    # Second solution has better Big O, but first performs better on LC test cases
    # Idea: make map where key is a common value between anagrams, put into right spot

    # Complexity: O(m*nlogn), where m is len(strs), n is average length of strings. Space: O(m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            group = groups.get(key, [])
            group.append(s)
            groups[key] = group
        return [groups[group] for group in groups]

    # Complexity: O(m*n), Space: O(m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None
        groups = {}
        for s in strs:
            alphabet = [0 for i in range(26)]
            for c in s:
                alphabet[ord(c) - ord('a')] += 1
            key = tuple(alphabet)
            group = groups.get(key, [])
            group.append(s)
            groups[key] = group
        return [groups[group] for group in groups]