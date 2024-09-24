# task1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split().pop())


# task2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = str(int(''.join(map(str, digits))) + 1)
        return [int(i) for i in s]
