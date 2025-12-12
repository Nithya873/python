class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c = "cat"
        d = "dog"
        k = list(s.split())
        t = 0
        li = []

        if len(pattern) != len(k):
            return False

        mp = {}
        used = set()

        for i in range(len(pattern)):
            ch = pattern[i]
            word = k[i]

            if ch in mp:
                if mp[ch] != word:
                    return False
            else:
                if word in used:
                    return False
                mp[ch] = word
                used.add(word)

            li.append(mp[ch])

        m = " ".join(li)
        if s == m:
            return True
        else:
            return False

           



   



        