'''
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, 
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 
Constraints:
2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

'''

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):      # if stack[-1] + asteroid < 0: 
                    stack.pop()
                elif stack[-1] == abs(asteroid):   # elif stack[-1] + asteroid == 0: 
                    stack.pop()
                    break
                elif stack[-1] > abs(asteroid):    # else:
                    break
            else:
                stack.append(asteroid) 
        return stack


# 長知識，我好菜 ><:
# Python 中 for 以及 while 可以像 if 一樣有個 else 區塊，當迴圈沒有中斷就會執行到 else 區塊。
# 換句話說，就是 esle 為 for loop 的其中一個部份，如果 break 就一併跳出，沒有的話就會執行到。

# Time complexity:??
# Strictly speaking the worst case scenario for this is O(n * m). 
# n representing the for loop iterations, and m being the potential iterations of the while loop. 
# Although, the time complexity is not really effected since the stack is implemented as a list so pop runs in constant time.


# Well, in this solution, the for loop has a time complexity of O(n) since it iterates through all the asteroids. On the other side, the nested while loop performs constant-time operations on the j index, where j is the index used to manage the asteroids array representing the final state after collisions.
# Since both loops are nested but not nested in the sense of iterating through all elements separately, the time complexity of the solution remain O(n). The while loop inside the for loop performs constant-time operations, and the for loop iterates through all n elements once, resulting in a linear time complexity of O(n) for the entire solution.
# Hope this helps
'''
Medium
# Array
# Stack
# Simulation
'''