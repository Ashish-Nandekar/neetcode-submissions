class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for str in strs:
            count = [0] * 26
            
            for c in str:
                count[ord(c) - ord('a')] += 1 # map value by performing substraction on ascii value
            
            key = tuple(count)

            # if key is not present assign empty list
            if key not in result:
                result[key] = []
            
            result[key].append(str)

        return list(result.values())
