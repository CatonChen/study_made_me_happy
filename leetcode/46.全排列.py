#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,size,depth,path,used,res):
            #terminator
            if depth==size:
                res.append(path.copy())
                return
            #current logic
            for i in range(size):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    #recursion    
                    dfs(nums,size,depth+1,path,used,res)
                    #reserve statu
                    used[i]=False
                    path.pop()

        res=[]
        size = len(nums)
        used = [False for _ in range(size)]
        dfs(nums,size,0,[],used,res)
        return res

# @lc code=end

