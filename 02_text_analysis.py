# 2. Text Analysis with Constraints
# Given a large paragraph of text, write a Python program that:
# • Counts the frequency of each word, ignoring common stop words (the, is, at, on, in, and,
# etc.).
# • Allows efficient querying, for example:
# • "Return the top 3 most frequent words starting with the prefix 'th'."
# • Optimize for performance.

import re
from collections import Counter, defaultdict
import heapq

# Define stop words
STOP_WORDS = {"the", "is", "at", "on", "in", "and", "a", "an", "of", "to", "with", "for", "by"}

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set()

class WordFrequencyAnalyzer:
    def __init__(self, text):
        self.word_count = Counter()
        self.trie_root = TrieNode()
        self._process_text(text)

    def _process_text(self, text):
        words = re.findall(r'\b[a-z]+\b', text.lower())
        filtered_words = [word for word in words if word not in STOP_WORDS]
        self.word_count.update(filtered_words)

        for word in self.word_count:
            self._insert_into_trie(word)

    def _insert_into_trie(self, word):
        node = self.trie_root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.add(word)  # Add word to all prefixes

    def top_n_with_prefix(self, prefix, n=3):
        node = self.trie_root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Get words with this prefix and their counts
        words_with_prefix = [(self.word_count[word], word) for word in node.words]
        # Return top n by frequency
        top_words = heapq.nlargest(n, words_with_prefix)
        return [word for freq, word in top_words]

# Example usage:
text = """
The theory of relativity was first proposed by Albert Einstein. 
This theory fundamentally changed the way we think about time, space, and gravity.
In the field of physics, the theory remains highly influential.
"""

analyzer = WordFrequencyAnalyzer(text)
print(analyzer.top_n_with_prefix("th", 3))  # Example query
