class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Approach 1 
        maxArea = 0 
        stack = [] 

        for i,h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:

                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index 
            stack.append((start,h))

        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea


        # Approach 2 - Using next smaller element from left and right
        rb = [0]*len(heights)
        lb = [0]*len(heights)
        n = len(heights)
        maxArea = 0 
        stack = []

        # finding the next smaller element on the right 
        # right to left

        stack.append(n-1)
        rb[n-1]=n 

        for i in range(n-2,-1,-1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if not stack:
                rb[i]=n
            
            else:
                rb[i] = stack[-1]
            stack.append(i)

        stack = []
        stack.append(0)
        lb[0]=-1 

        for i in range(1,n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if not stack:
                lb[i]= -1

            else:
                lb[i] = stack[-1]
            stack.append(i)


            # finding max area 

        for i in range(len(heights)):
            width = rb[i] - lb[i] - 1
            area = heights[i] * width 

            if area > maxArea:
                maxArea = area
        
        return maxArea
        

