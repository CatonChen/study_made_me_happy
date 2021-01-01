#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # count,m,prev = 0 , len(flowerbed),-1    #初始化 计算0，数组长度m，prev -1
        # for i in range(m):
        #     if flowerbed[i]==1:
        #         if prev<0:
        #             count = count + (i//2) #// 整数除法  / 浮点数除法
        #         else:
        #             count = count + ((i-prev-2)//2)
        #         prev = i
        # # print(prev)
        # if prev<0:
        #     count=count+((m+1)//2) 
        #     # print(count)
        # else:
        #     count=count + ((m-prev-1)//2)
        #     # print(count)
        
        # return count>=n

        
        flowerbed.append(0)
        l=flowerbed
        for i in range(len(l)-1):
            if l[i-1]+l[i]+l[i+1]==0:   #根据 i-1 ， i， i+1 三者之和是否=0 来决定是否种花
                l[i]=1
                n-=1
        # print(l[i-1]+l[i]+l[i+1])
        return n<=0        

# @lc code=end

