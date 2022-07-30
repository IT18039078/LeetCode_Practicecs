class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        list_count = {}
        copy = arr
        copy.sort()
        count = k 
        sort_data = []
        print(copy)
#         travers all the elements
        if(len(arr) >= 1 and len(arr) <= 10**5 and k >= 0 and k <= len(arr)):
            print('Go ahead')
        else:
            return False

        for i in arr:
            # if(arr[i] >= 1 and arr[i] <= 10**9):
                list_count[i]= arr.count(i)
                sort_data = sorted(list_count.items(), key=lambda x: x[1], reverse=False)

        for i in sort_data:
            if(count > 0):
                if(i[1] <= count and count != 0 and count != 1):
                    number = i[0]
                    num = 0
                    # this code to remove all the occurence with particular value in the list
                    try:
                        while True:
                            copy.remove(number)
                            num = num +1 
                    except ValueError:
                        pass
                
                    count -= num
                    print(count, number, num)
                elif(count == 1 ):
                    num = 0
                    number = i[0]
                    print(number)
                    copy.remove(number)
                    num = num +1 
                    count -= num
        return sort_data, copy, len(set(copy)) # len(set(copy)) - this is the way of finding count of unique values in the lsit







arr = [4,5,5]
k= 1
print(Solution.findLeastNumOfUniqueInts(Solution, arr, k))