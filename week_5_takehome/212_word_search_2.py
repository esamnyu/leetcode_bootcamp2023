class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = set()
        self.trie = Trie()
        
        # Build Trie
        for word in words:
            self.trie.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, self.trie.root, "")
        
        return list(self.result)
    
    def dfs(self, board, i, j, node, path):
        # If out of bounds or visited or not in Trie, stop.
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return
        
        # Update path and mark as visited
        char = board[i][j]
        board[i][j] = "#"
        path += char
        node = node.children[char]
        
        # If current path is a word, add to result
        if node.is_end_of_word:
            self.result.add(path)
        
        # Explore all possible neighbors
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            self.dfs(board, x, y, node, path)
        
        # Backtrack
        board[i][j] = char

# Your Solution object will be instantiated and called as such:
# obj = Solution()
# result = obj.findWords(board, words)
