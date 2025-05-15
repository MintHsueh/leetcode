# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs):
        # strs_sorted = list(map(sorted, strs))
        # strs_sorted = list(map(lambda x: "".join(x), strs_sorted))
        strs_sorted = list(map(lambda x: "".join(sorted(x)), strs))

        groups = {}
        for i in range(len(strs_sorted)):
            if strs_sorted[i] in groups:
                groups[strs_sorted[i]].append(strs[i])
            else:
                groups[strs_sorted[i]] = [strs[i]]
        
        output = [x for x in groups.values()]
        return output
    
    # Time complexity: O(m∗nlog⁡n)
    # Space complexity: O(m∗n)
    # Where 𝑚 m is the number of strings and 𝑛 n is the length of the longest string.
    def groupAnagrams_2(self, strs):
        groups = {}
        for string in strs:
            string_sorted = "".join(sorted(string)) # dic的key不能為list
            if string_sorted in groups:
                groups[string_sorted].append(string)
            else:
                groups[string_sorted] = [string]
        
        output = list(groups.values())  # output = [x for x in groups.values()]
        return output


'''
# python note:

a = 'abc'
# a.sort()   # AttributeError: 'str' object has no attribute 'sort'
print(sorted(a))    # ['a', 'b', 'c']
print([a])          # ['abc']
print(list(a))      # ['a', 'b', 'c']
print(''.join(sorted(a)))  # abc

'''