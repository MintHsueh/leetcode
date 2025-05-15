'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

'''

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
          
        def backtrack(index, current_comb):
            if index == len(digits):
                result.append(current_comb)
                return
            for letter in mapping[digits[index]]:
                backtrack(index + 1, current_comb + letter)

        backtrack(0, "")
        return result
      
print(Solution().letterCombinations(digits="234"))


'''
Medium

#Hash Table  #String  #Backtracking

Time complexity: O(4^n)
The time complexity of this approach is O(4^n) where n is the number of digits in the input string. 
This is because each digit can map to up to 4 letters in the worst case, and there are n digits in the input.

Space complexity: O(n)
The space complexity is O(n) as we are using recursion and the maximum depth of the recursion is n. 
Additionally, we are using a result list to store the combinations, which can also take up to O(n) space in the worst case.
'''