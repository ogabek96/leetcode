class Codec:
    data = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = 0
        if len(self.data.keys()) == 0:
            key = 0
        else:
            key = list(self.data.keys())[-1] + 1
        self.data[key] = longUrl
        return key
    def decode(self, shortUrl: str) -> str:
        print(shortUrl)
        return self.data[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))