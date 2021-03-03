class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        check = 0
        matches = 0
        if ruleKey == 'type':
            check = 0
        if ruleKey == 'color':
            check = 1
        if ruleKey == 'name':
            check = 2
        for itm in items:
            if itm[check] == ruleValue:
                matches+=1
        return matches