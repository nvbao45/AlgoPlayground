You are given a positive integer `days` representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array `meetings` of size `n` where, `meetings[i] = [start_i, end_i]` represents the starting and ending days of meeting `i` (inclusive).  

Return the count of days when the employee is available for work but no meetings are scheduled.

**Note:** The meetings may overlap.

**Example 1:**  
<pre>
<b>Input:</b> days = 10, meetings = [[5,7], [1,3], [9,10]]  
<b>Output:</b> 2  
<b>Explanation:</b>  
There is no meeting scheduled on the 4<sup>th</sup> and 8<sup>th</sup> days.
</pre>

**Example 2:**
<pre>
<b>Input:</b> days = 5, meetings = [[2,4], [1,3]]
<b>Output:</b> 1
<b>Explanation:</b>
There is no meeting scheduled on the 5<sup>th</sup> day.
</pre>

**Example 3:**
<pre>
<b>Input:</b> days = 6, meetings = [[1,6]]
<b>Output:</b> 0
<b>Explanation:</b>
Meetings are scheduled for all working days.
</pre>

**Constraints:**
- <code>1 <= days <= 10<sup>9</sup></code>
- <code>1 <= meetings.length <= 10<sup>5</sup></code>
- <code>meetings[i].length == 2</code>
- <code>1 <= meetings[i][0] <= meetings[i][1] <= days</code>


<details>
    <summary><b>Hint</b></summary>
    <ul>
        <li>Merge the overlapping meetings and sort the new meetings timings.</li>
        <li>Return the sum of difference between the end time of a meeting and the start time of the next meeting for all adjacent pairs.</li>
    </ul>
</details>  
  
---

**Solution**
```python
class Solution:
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort intervals list by first element in subarray  
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        for current in intervals[1:]:
            last_merged = merged[-1]
            # If the current interval overlaps with the last merged one, merge them
            if current[0] <= last_merged[1] + 1:
                last_merged[1] = max(last_merged[1], current[1])
            else: 
                # Otherwise, add the current interval to merged list
                merged.append(current)

        return merged
        
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = self.merge_intervals(meetings)

        working_days = 0

        # Add the days before the first meeting
        working_days += meetings[0][0] - 1 

        for i in range(1, len(meetings)):
            # Calculate the gap between the end of the last meeting and the start of the current meeting
            working_days += meetings[i][0] - meetings[i - 1][1] - 1
        
        # Add the days after the last meeting
        working_days += days - meetings[-1][1]
        
        return working_days
```