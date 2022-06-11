class Solution(object):
    def twoSum(self, nums, target):

        hold={}
        for i,val in enumerate(nums):
            if val in hold:
                return (hold[val],i)
            else:
                hold[target-val]= i
        return []
            
            
# print(twoSum())
