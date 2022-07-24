class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        result = False
        if(x < 0):
            resul = False
        else:

            # whole idea is to 
            #   1. chenge the the number into list, 
            #   2. reversed it, 
            #   3. changed it to integer  
            #   4. and finally compare compare 
            # change the integer to list
            copy = [int(a) for a in str(x)]
            # reverse the list
            reversed_list = copy[::-1]


            # change list into string 
            string = [str(integer) for integer in copy ]
            copy_one = ''.join(string)
            # chenge string into integer
            origin_integer = int(copy_one)

            string2 = [str(integer) for integer in reversed_list]
            copy_two = ''.join(string2)
            reversed_integer = int(copy_two)
            
            if(origin_integer == reversed_integer):
                result = True
        
        return result;

num = 121
res  = Solution.isPalindrome(Solution, num)
print(res)


# here i have faced one problem that i put the integer convertion before check the
# number is integer but that could put else condion when the negtive number is checked