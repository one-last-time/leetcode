class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        next_index = 0
        index_map = dict()
        res = []
        for s in strs:
            sum = 0
            for i in s:
                sum += pow((ord(i) - ord('a') + 1) , 12) # 3^12/2^12 > 100
            index = index_map.get(sum)
            if index is not None:
                res[index].append(s)
            else:
                index_map[sum] = next_index
                next_index += 1
                res.append([s])
        return res


