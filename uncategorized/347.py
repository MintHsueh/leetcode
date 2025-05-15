#　347. Top K Frequent Elements

class Solution:
    # Time Complexity : O(n) + O(n * log(n)) = O(n * log(n))
    # Space Complexity : O(n)
    def topKFrequent(self, nums, k: int):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        count = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))  
        # count = {k: v for k, v in sorted(count.items(), key = lambda x: x[1], reverse = True)}
        result = list(count.keys())[:k]      # [x for x in count][:k]
        return result               

'''
# python note
a = {1:3, 5:4, 3:1}

# 'dict' object has no attribute 'sort'  只能用sorted

print(a.items())            # dict_items([(1, 3), (5, 4), (3, 1)])
print(sorted(a.items()))    # [(1, 3), (3, 1), (5, 4)]  
print(sorted(a))            # [1, 3, 5]
print([x for x in a])       #[1, 5, 3]

b = {k: v for k, v in sorted(a.items(), key = lambda item: item[1], reverse=True)}
print(b)    # {5: 4, 1: 3, 3: 1}

c = {k: v for k, v in sorted(a.items())}    
print(c)    # {1: 3, 3: 1, 5: 4}

d = [1, 5, 3]
print([d[x] for x in range(2)]) # [1, 5]

e = [(1, 3), (3, 1), (5, 4)] 
print(dict(e))  # {1: 3, 3: 1, 5: 4}
'''