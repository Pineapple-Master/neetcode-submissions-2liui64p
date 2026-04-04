class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = None
        sellDay = None
        maxProfit = 0

        for i in range(0, len(prices), 1):
            
            profit = 0
            newPrice = prices[i]
            if buyDay is None:
                buyDay = newPrice
                sellDay = newPrice
                profit = 0
            else:
                if newPrice < buyDay:
                    buyDay = newPrice
                    sellDay = newPrice
                elif newPrice > sellDay:
                    sellDay = newPrice

                profit = sellDay - buyDay
                if(profit > maxProfit):
                    maxProfit = profit
                
        
        return maxProfit
                    
                
            
        