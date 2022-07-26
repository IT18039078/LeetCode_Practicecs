from asyncio.windows_events import NULL


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        biggest_prefix = ''
        stop = 1
        length = 0
        list_length = len(strs)
        # first have to findout the which string is smaller one - 
        # because that have the possiblity to be biggest prefix
        if(list_length != 0):
            if(len(strs[0]) < len(strs[1])):
                if(len(strs[0]) < len(strs[2])):
                    biggest_prefix =  strs[0] 
            elif(len(strs[1]) < len(strs[2])):
                biggest_prefix = strs[1]
            else:
                biggest_prefix = strs[2]

        length = len(biggest_prefix)
        string_length = 0
        # code for the contraints
        if(  (len(strs) <= 200 and len(strs) >= 1)):
            for i in range(len(strs)):
                string_length = len(strs[i])
                if(( string_length >= 0 and string_length <= 200) and strs[i].islower()):
                    # finout the longest common string in the list
                    while(stop == 1 and length > 0):
                        if(biggest_prefix in strs[0] and biggest_prefix in strs[1] and biggest_prefix in strs[2]):
                            length = 0
                            stop = 0 
                            return biggest_prefix           
                        else:
                            biggest_prefix = biggest_prefix[:-1]
                            length = len(strs) - 1
        else:
            return "string is not  good"
        if(len(biggest_prefix) == 0):
            return ""
        else:
            return biggest_prefix
strs = ["Flower","flow","flight"]
print(Solution.longestCommonPrefix(Solution, strs))