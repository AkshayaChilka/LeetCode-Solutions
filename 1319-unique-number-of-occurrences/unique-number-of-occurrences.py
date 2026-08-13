class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """hashmap={}
        for num in arr:
            hashmap[num]=hashmap.get(num,0)+1
        return len(hashmap.values())==len(set(hashmap.values()))"""

        #from collections import Counter
        
        # Step 1: Count occurrences
        freq = Counter(arr)
        
        # Step 2: Check uniqueness
        return len(freq.values()) == len(set(freq.values()))
        

        



