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
            # for a practice purpose i checked whether theintiger is can change into string 
            # as_string = str(origin_integer)
            string2 = [str(integer) for integer in reversed_list]
            copy_two = ''.join(string2)
            reversed_integer = int(copy_two)
            
            if(origin_integer == reversed_integer):
                result = True
        
        return result;

num = 1214
res  = Solution.isPalindrome(Solution, num)
print(res)


# here i have faced one problem that i put the integer convertion before check the
# number is integer but that could put else condion when the negtive number is checked

#############################       QUESTION      #############################  
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 