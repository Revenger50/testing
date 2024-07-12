class Solution:
    def averageWaitingTime(self, customers):
        starting_time = 0
        finishing_time = 0
        waiting_time = 0
        result = 0
        for x in customers:
            if finishing_time > x[0]:
                starting_time = finishing_time
            else:
                starting_time = x[0]
            finishing_time = starting_time + x[1]
            waiting_time = finishing_time - x[0]

            result += waiting_time



        
        return result / len(customers)

customers = [[5, 2], [5, 4], [10, 3], [20, 1]]
solution = Solution()
print(solution.averageWaitingTime(customers))  # Expected output: 3.25
