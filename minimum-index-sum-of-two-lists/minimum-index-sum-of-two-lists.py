class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {s: i for i, s in enumerate(list1)}
        
        min_index_sum = float('inf')
        result = []
        
        for j, s in enumerate(list2):
            if s in index_map:
                i = index_map[s]
                index_sum = i + j
                
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [s]
                elif index_sum == min_index_sum:
                    result.append(s)
        
        return result