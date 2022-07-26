class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allowed_string = ['(',')','[',']','{','}']
        counter = 0
        print(len(s))
        if any(x in allowed_string for x in s):
            while(counter < len(s)):
                print(counter)
                if((s[counter] == '(' and s[counter+1] == ')') or (s[counter] == '{' and s[counter+1] == '}') or (s[counter] == '[' and s[counter+1] == ']')):
                    print(s[counter] + s[counter+1])
                    if(counter == len(s) -2):
                        return True
                    counter += 2
                    
                else:
                    return False    
        

s = "()"
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