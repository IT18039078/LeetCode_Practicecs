class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        biggest_prefix = strs[0]
        list_length = len(strs)
        # first have to findout the which string is smaller one - 
        # because that have the possiblity to be biggest prefix
        if(list_length > 1):
                for i in range(len(strs)):
                    if(len(strs[i]) < len(biggest_prefix)):
                        biggest_prefix = strs[i]

                length = len(biggest_prefix)
                string_length = 0
                # code for the contraints
                if(  (len(strs) <= 200 and len(strs) >= 1)):
                    for i in range(len(strs)):
                        string_length = len(strs[i])
                        if(( string_length >= 0 and string_length <= 200) and strs[i].islower()):
                            # finout the longest common string in the list
                            for i in range(len(strs)):
                                string = strs[i]
                                if(string.startswith(biggest_prefix)):
                                    biggest_prefix = biggest_prefix
                                else:
                                    biggest_prefix = biggest_prefix[:-1]                                
                                
                        else:
                            if(strs[i] == ''):
                                biggest_prefix = ' '
        

        
        if(len(biggest_prefix) ==  1 and biggest_prefix == " "):
            biggest_prefix = ' '
        elif(biggest_prefix == ""):
            biggest_prefix = ' '

        return biggest_prefix

strs = ["flower","fkow"]
print(Solution.longestCommonPrefix(Solution, strs))