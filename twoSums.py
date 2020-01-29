# Takes list of ints and finds the indices of the two
# numbers which sum together to reach a target number

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashTable = {}

        for i in range(len(nums)):
            num = nums[i]
            leftover = target - num

            if leftover in HashTable.keys():
                return[HashTable[leftover], i]
            else:
                HashTable[num] = i
        return
