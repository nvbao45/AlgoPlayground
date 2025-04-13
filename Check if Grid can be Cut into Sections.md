# LeetCode 3394. Check if Grid can be Cut into Sections
#### Problem Link: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections
#### Difficulty: <span style="color:#ffb800">Medium</span>  
#### Topics: Array, Sorting

---
## Description  

You are given an interger `n` representing the dimensions of an `n x n` grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates `rectangles`, where `rectangles[i]` is in the form <code>[start<sub>x</sub>, start<sub>y</sub>, end<sub>x</sub>, end<sub>y</sub>]</code>, representing a rectangle on the grid. Each rectangle í defined as follows:
- <code>(start<sub>x</sub> start<sub>y</sub>)</code>: The bottom-left corner of the rectangle.
- <code>(end<sub>x</sub> end<sub>y</sub>)</code>: The top-right corner of the rectangle.

**Note** that the rectangles do not overlap. Your task is to determine if it is possible to make **either two horizontal or two vertical cuts** on the grid such that:
- Each of the three resulting sections formed by the cuts contains **at least** one rectangle.
- Every rectangle belongs to **exactly** one section.

Return `true` if such cuts can be made; otherwise, return `false`.

**Example 1:**
<pre>
<b>Input:</b> n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
<b>Output:</b> true
<b>Explanation:</b>
<img src="images/3394-1.png" />
The grid is shown in the diagram. We can make horizontal cuts at `y = 2` and `y = 4`. Hence, output is true.
</pre>

**Example 2:**
<pre>
<b>Input:</b> n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
<b>Output:</b> true
<b>Explanation:</b>
<img src="images/3394-2.png" />
We can make vertical cuts at `x = 2` and `x = 3`. Hence, output is true.
</pre>

**Example 3:**
<pre>
<b>Input:</b> n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
<b>Output:</b> false
<b>Explanation:</b>
We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.
</pre>

**Constraints:**
- <code>1 <= n <= 10<sup>9</sup></code>
- <code>3 <= rectangles.length <= 10<sub>5</sub></code>
- <code>0 <= rectangles[i][0] < rectangles[i][2] <= n</code>
- <code>0 <= rectangles[i][1] < rectangles[i][3] <= n</code>
- No two rectangles overlap.

<details>
<summary><strong>Hint 1</strong></summary>
<ul>
    <li>For each rectangle, consider ranges <code>[start_x, end_x]</code> and <code>[start_y, end_y]</code> separately.</li>
    <li>For x and y directions, check whether we can split it into 3 parts.</li>
</ul>
</details>

---
## Approach
1. For each rectangle, extract the horizontal range `[start_x, end_x]` and the vertical range `[start_y, end_y]` separately.
2. Merge overlapping horizontal and vertical ranges to simplify the grid representation.
3. Verify if the number of merged horizontal or vertical ranges is at least 3, which would allow for the required cuts.

---
## Code

**Time Complexity:** O(NlogN), sine we are sorting the lines.   
**Space Complexity:** O(N), where N is the number of rectangles.

**Python Code:**
[Playground](https://leetcode.com/playground/kQhYW9fb)
```python
from typing import List

class Solution:
    def mergeLine(self, lines: List[List[int]]) -> List[List[int]]:
        lines.sort(key=lambda x: x[0])
        merged_lines = [lines[0]]
        for i in range(1, len(lines)):
            if lines[i][0] < merged_lines[-1][1]:
                merged_lines[-1][1] = max(merged_lines[-1][1], lines[i][1])
            else:
                merged_lines.append(lines[i])
        return merged_lines

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal_lines = [[rect[0], rect[2]] for rect in rectangles]
        vertical_lines = [[rect[1], rect[3]] for rect in rectangles]

        horizontal_lines = self.mergeLine(horizontal_lines)
        vertical_lines = self.mergeLine(vertical_lines)

        return len(horizontal_lines) >= 3 or len(vertical_lines) >= 3
```