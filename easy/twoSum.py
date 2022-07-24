class Solution(object):
    def towSum(self,nums, target):

        # for loop for access first element
        for i in range(len(nums)):
            e = i + 1;
            for l in range(e,len(nums)):
                add = nums[i] + nums[e]
                if(add == target):
                    print([i, l])
                    break


number = [2,7,6,4]
targets = 9
Solution.towSum(Solution,number, targets)

# SLUTION OF LEET CODE
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         count = len(nums)
#         for i in range(count):
#             e = i + 1;
#             for l in range(e,count):
#                 add = nums[i]  + nums[l]
#                 if(add == target):
#                     return [i,l]
#                     break