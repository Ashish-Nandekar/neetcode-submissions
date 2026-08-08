class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result ={}

        for str in strs:
            sortedString = ''.join(sorted(str))

            if sortedString not in result:
                result[sortedString] = []

            result[sortedString].append(str)

        return list(result.values())