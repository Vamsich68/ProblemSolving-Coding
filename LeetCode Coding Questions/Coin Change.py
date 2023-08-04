
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
solution=Solution()
coins=[2,5,10]
amount=12
print(solution.coinChange(coins,amount))

'''
        [2,5,10] amount = 12
        dp=[0,x,x,x,x,x,x,x,x,x,x,x,x]
        loop-1 : 
            dp=[0,x,1,x,x,x,x,x,x,x,x,x,x]
        '''

    #def coinChange(self, coins: List[int], amount: int) -> int:
'''
        coun = 0
        coins.sort()
        i = len(coins) - 1
        while amount > 0 and i >= 0:
            if amount < coins[i]:
                i -= 1
            temp = amount % coins[i]
            #print(coins[i], amount, temp)
            # print(i,temp)
            res = amount - temp
            # print(res)
            coun += res // coins[i]
            #print(coun,i)
            amount = temp
        if amount==0:
            return coun
        else:
            return -1
        '''
    
