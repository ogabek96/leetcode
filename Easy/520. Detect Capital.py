class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        if word[0].upper() == word[0] and (word[1:].lower() == word[1:]):
            return True
        return False