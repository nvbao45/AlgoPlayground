
from typing import List

class Solution:
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged[-1]
            if current[0] <= last_merged[1] + 1:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged.append(current)

        return merged
        
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = self.merge_intervals(meetings)

        working_days = 0
        working_days += meetings[0][0] - 1 
        for i in range(1, len(meetings)):
            working_days += meetings[i][0] - meetings[i - 1][1] - 1
        working_days += days - meetings[-1][1]
        return working_days


sol = Solution()
days = 8
meetings = [[3,4],[4,8],[2,5],[3,8]]
merged_meetings = sol.merge_intervals(meetings)
print(merged_meetings)  # Expected output: [[1, 4]]
result = sol.countDays(days, meetings)

print(result)  # Expected output: 2