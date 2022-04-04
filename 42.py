class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = []
        left_max.append(height[0])

        for i in range(1, len(height)):
            
            left_max.append(max(height[i], left_max[i-1]))

        right_max = []
        right_max.insert(0, height[-1])

        for i in range(len(height)-2,-1,-1):
            
            right_max.insert(0, max(height[i], right_max[0]))

        numbers=[]
        
        for i in range(len(height)):
            
            numbers.append(min(left_max[i], right_max[i])-height[i])

        return(sum(numbers))
