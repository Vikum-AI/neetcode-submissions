class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            
            for c in s:
                i = ord(c) - ord('a')
                key[i] +=1 
            
            key = tuple(key)
            hash_map[key].append(s)

        return list(hash_map.values())