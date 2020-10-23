class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        def comp(w):
            return freq[w]
        for word in words:
            if freq.get(word) != None:
                freq[word] += 1
            else:
                freq[word] = 0
        unsortedList = sorted(list(freq.keys()))
        sortedList = sorted(unsortedList, key=comp, reverse=True)
        return sortedList[0:k]