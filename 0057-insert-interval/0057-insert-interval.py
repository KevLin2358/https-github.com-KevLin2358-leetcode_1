class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start = newInterval[0]
        end = newInterval[1]

        i = 0 # traversing through intervals arr
        length = len(intervals)
        
        while i < length and start > intervals[i][1]:
            res.append(intervals[i])
            i+=1
            #print("1 while")
        
        while i < length and end >= intervals[i][0]:
            if start > intervals[i][0]:
                start = intervals[i][0]
            
            if end < intervals[i][1]:
                end = intervals[i][1]
                
            i+=1
            #print("2 while")

        
        res.append([start,end])
        
        while i < length:
            res.append(intervals[i])
            i+=1
            #print("3 while")

        return res;