class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allowed_string = ['(',')','[',']','{','}']
        copy = ''
        if any(x in allowed_string for x in s):
            round = 0
            i = j = f= 0
            list1=[]
            copy_list =[]
            list1[:0]=s
            copy_list = list1
            must_round = len(copy_list)/2
            for x in range(len(list1)):
                for y in range(len(list1)):
                    if(copy_list != [] and f < len(copy_list)):
                        print(len(copy_list),i,f)
                        if(copy_list[i] == '(' and copy_list[f + 1] == ')'):
                            print(copy_list.pop(i))
                            print(copy_list.pop(f))
                            round += 1
                            i =  f = 0
                            print(copy_list,i,f)                   
                        elif(copy_list[i] == '[' and copy_list[f+1] == ']'):
                            print(copy_list.pop(i))
                            print(copy_list.pop(f))
                            round += 1
                            i = f=  0
                            print(copy_list)
                        elif(list1[i] == '{' and list1[j+1] == '}'):
                            print(copy_list.pop(i))
                            print(copy_list.pop(f))
                            round += 1
                            i = f=  0
                            print(copy_list)
                            print(round)
                        else:
                            f += 1

        if(round == must_round):
            return True
        else:
            return  False
                        
                
                        
             

        

s = "[[[[((({{{])})}]]])}"
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