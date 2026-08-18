class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
        

        if not strs:
            return ""
        
        # Loop through characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Compare with the same position in all other strings
            for s in strs[1:]:
                # If index out of range OR mismatch → stop
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]