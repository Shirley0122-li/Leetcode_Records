class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        meeting = []
        res = 0
        for s,e in intervals:
            if meeting and s >= meeting[0]:
                heapq.heappop(meeting)
            
            heapq.heappush(meeting, e)
            res = max(res, len(meeting))
        
        return res

