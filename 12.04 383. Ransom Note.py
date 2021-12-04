class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lst = collections.Counter(magazine)
        for i in ransomNote:
            lst[i] -= 1
            if lst[i] < 0:
                return False
        return True
