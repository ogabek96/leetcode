class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hmap = defaultdict(int)
        for n in arr:
            hmap[n]+=1
        dist = []
        for key, val in hmap.items():
            if val == 1:
                dist.append(key)
        if len(dist) >= k:
            return dist[k - 1]
        return ""