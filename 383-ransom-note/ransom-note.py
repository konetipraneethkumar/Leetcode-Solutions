class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashTable = {}
        hashTable1 = {}
        for ch in ransomNote:
            hashTable[ch]  = hashTable.get(ch,0) + 1
        for ch in magazine:
            hashTable1[ch]  = hashTable1.get(ch,0) + 1
        for key in hashTable:
            if key not in hashTable1 or hashTable[key] > hashTable1[key]:
                return False
        return True



