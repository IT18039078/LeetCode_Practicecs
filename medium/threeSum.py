class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         let assum the length of array is 6
        result  = []
        result2 =[]
        fresult  = []
        same = all(elem == 0 for elem in nums)
        # if all the numbers are same then we dont need to actually calculate and send 
        # anyway the answer will be 0 
        if(same):
            result.append([0,0,0])
            result.sort()
            return result
        else:
            if(len(nums) <= 3 ):
                add = nums[0] + nums[1] + nums[2]
                if(add == 0):
                    fresult.append([nums[0] , nums[1] , nums[2]])
                    fresult.sort()
            else:
                for i in range(len(nums)):
                    print(i)
                    for e in range(len(nums)):
                        if( e == i):
                            continue
                        else:
                            # this logic should be think very carefully
                            if(e+1 < len(nums) & e+2 < len(nums)):
                                add = nums[i] + nums[e + 1] + nums[e+2]
                                if(add == 0):
                                    result.append([nums[i],nums[e+1],nums[e+2]])
        
        for i in range(len(result)):
            result[i].sort()
                                    
        
        for i in result: 
            if i not in fresult:
                fresult.append(i)
        
        return fresult


nums = [-1,0,1,0]
solution = []
solution = Solution.threeSum(Solution, nums)
print(solution)