# NEW PROGRAM COMMENT 
# Runtime: 47 ms, faster than 72.84% of Python online submissions for Richest Customer Wealth.
# Memory Usage: 13.3 MB, less than 93.10% of Python online submissions for Richest Customer Wealth.

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = len(accounts)
        n= 0
        totals = []
        if(m >= 1):
            for i in range(m):
                n = len(accounts[i])
                if(n <= 50):
                    total = 0
                    total = sum(accounts[i])
                    
                    totals.append(total)
        return max(totals)

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(Solution.maximumWealth(Solution, accounts))


# OLD WAY OF SOLVED PROBLEM BUT THE FAST DETAILS IS SHOWING IT IS LESS PERFORMING METHOD 
# THE NEW ONE IN UP IS BETTER BECAUSE OF USING AGREGATE FRUNCTION sum() for calculate total
                        # MACHINE COMMENTS ON THE PROGRAME
# Runtime: 55 ms, faster than 56.43% of Python online submissions for Richest Customer Wealth.
# Memory Usage: 13.4 MB, less than 75.57% of Python online submissions for Richest Customer Wealth.

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m = len(accounts)
        n= 0
        totals = []
        if(m >= 1):
            for i in range(m):
                n = len(accounts[i])
                if(n <= 50):
                    total = 0
                    for j in range(n):
                        total += accounts[i][j]
                    
                    totals.append(total)
        return max(totals)