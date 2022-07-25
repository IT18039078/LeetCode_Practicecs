class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        biggest_prefix   = ''
        # first have to findout the which string is smaller one - 
        # because that have the possiblity to be biggest prefix
        if(len(strs[0]) < len(strs[1])):
            if(len(strs[0]) < len(strs[2])):
                biggest_prefix =  strs[0] 
        elif(len(strs[1]) < len(strs[2])):
            biggest_prefix = strs[1]
        else:
            biggest_prefix = strs[2]

        
        return biggest_prefix
strs = ["flower","flow","flight"]
print(Solution.longestCommonPrefix(Solution, strs))