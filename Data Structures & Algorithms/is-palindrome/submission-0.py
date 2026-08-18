class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first intuition
        temp = "".join([char for char in s if char.isalnum()]).lower()
        reverse = temp[::-1]
        if temp != reverse:
            return False
        else:
            return True

