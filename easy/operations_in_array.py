class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        allowedstring = ['X++','++X','X--','--X']
        if(len(operations) >= 1 and len(operations) <= 100):
            if any(x in allowedstring for x in operations):
                for i in range(len(operations)):
                    if(operations[i] == 'X++' or operations[i] == '++X'):
                        x += 1
                    elif(operations[i] == 'X--' or operations[i] == '--X'):
                        x -= 1
        return x

operations = ["--X","X++","X++"]
print(Solution.finalValueAfterOperations(Solution, operations))