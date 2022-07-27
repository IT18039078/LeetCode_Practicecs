class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allowed_string = ['(',')','[',']','{','}']
        copy = ''
        if any(x in allowed_string for x in s):
            copy  = s
            length = len(copy)
            i = j = 0
            list1=[]
            list1[:0]=s
            while(length > 0 and j < length):
                    if(list1[i] == '(' and list1[j + 1] == ')'):
                        print(list1.pop(i))
                        print(list1.pop(i))
                        i = j = 0
                        length = len(list1)
                        print(list1)
                    elif(list1[i] == '[' and list1[j+1] == ']'):
                        print(list1.pop(i))
                        print(list1.pop(i))
                        i = j = 0
                        length = len(list1)
                        print(length)
                    elif(list1[i] == '{' and list1[j+1] == '}'):
                        print(list1.pop(i))
                        print(list1.pop(i))
                        i = j = 0
                        length = len(list1)
                        print(length)
                    j += 1;
             

        

s = "([])"
print(Solution.isValid(Solution, s))







# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.