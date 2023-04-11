class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = 1000
        disband=0
        for item  in strs:
            n = min(len(item), n)
        for i in range(n):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if not strs[j][i] == c:
                    disband = 1
                    break
            if disband:
                break
            else:
                res+=str(c)
        return res