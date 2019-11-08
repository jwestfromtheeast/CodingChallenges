# To signal the end of a word, you can use either a boolean flag in your node class or a termination character in adj
# A termination character would work as so: Search for it in adj and if you find it, you are currently at a word
# If you need to do prefix-based lookups, tries are the way to go. Else, use hash tables
class Node:
    def __init__(self, val):
        self.val = val
        self.adj = {}
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if not c in curr.adj:
                curr.adj[c] = Node(c)
            curr = curr.adj[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if not c in curr.adj:
                return False
            curr = curr.adj[c]
        return True if curr.isWord else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if not c in curr.adj:
                return False
            curr = curr.adj[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)