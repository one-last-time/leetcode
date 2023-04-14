class Solution:
    def longestPalindrome(self, words) -> int:
        w = {}
        for word in words:
            w[word] = w.get(word, 0) + 1
        res = 0
        p_w = 0
        for word in words:
            r_w = word[::-1]
            if r_w == word and w.get(word):
                res += (w.get(word) // 2) * 2 * 2
                p_w += w.get(word) % 2
                w[word] -= (w.get(word) // 2) * 2
            elif w.get(word) and w.get(r_w) and word != r_w:
                w[word] -= 1
                w[r_w] -= 1
                res += 4

        if p_w:
            res += 2

        return res


Solution().longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"])