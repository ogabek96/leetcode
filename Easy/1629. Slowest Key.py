class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keys = {}
        lastKeyDuration = 0
        for i in range(len(keysPressed)):
            if keysPressed[i] in keys:
                if keys[keysPressed[i]] < releaseTimes[i] - lastKeyDuration:
                    keys[keysPressed[i]] = releaseTimes[i] - lastKeyDuration
            else:
                keys[keysPressed[i]] = releaseTimes[i] - lastKeyDuration
            lastKeyDuration = releaseTimes[i]
        keysList = sorted(list(keys.keys()), reverse=True)
        def sorter(itm):
            return keys[itm]
        keysList = sorted(keysList, key=sorter, reverse=True)
        return keysList[0]
