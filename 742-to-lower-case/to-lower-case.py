class Solution:
    def toLowerCase(self, s: str) -> str:
        """return s.lower()"""
        
        result = []
        for ch in s:
            # Check if character is uppercase (ASCII range 'A'–'Z')
            if 'A' <= ch <= 'Z':
                # Convert to lowercase by adding 32 to ASCII code
                result.append(chr(ord(ch) + 32))
            else:
                result.append(ch)
        return "".join(result)