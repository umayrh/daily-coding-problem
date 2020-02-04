"""
Implement an autocomplete system. That is, given a query string `s` and a set of all possible query strings,
return all strings in the set that have `s` as a prefix.

For example, given the query string `de` and the set of strings `[dog, deer, deal]`, return `[deer, deal]`.

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

from typing import Dict
Map = Dict[str, Dict]


class UncompressedTrie:
    def __init__(self):
        self.trie: Map = {}

    def add_all(self, words):
        for word in words:
            self.add(word)

    def add(self, word: str):
        trie_level = self.trie
        for idx in range(len(word)):
            if not word[idx] in trie_level:
                trie_level[word[idx]]: Map = {}
            trie_level = trie_level[word[idx]]
        trie_level["*"] = {word: {}}

    def find(self, prefix: str):
        if not self.trie:
            return set()
        trie_level = self.trie
        for idx in range(len(prefix)):
            if not prefix[idx] in trie_level:
                return set()
            trie_level = trie_level[prefix[idx]]
        # find all words under this sub-trie
        result = set()
        self._find(trie_level, result)
        return result

    def _find(self, trie: Map, result: set):
        if not trie:
            return
        if '*' in trie:
            for key in trie['*'].keys():
                result.add(key)
        for key in trie:
            self._find(trie[key], result)


if __name__ == "__main__":
    trie = UncompressedTrie()
    trie.add("dog")
    assert "dog" in trie.find("dog")

    trie.add("deer")
    trie.add("deal")
    assert set(["deer", "deal"]).issubset(trie.find("de"))
