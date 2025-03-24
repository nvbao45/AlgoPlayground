# LeetCode 3191. Minimum Operations to Make Binary Array Elements Equal to One I
#### Problem Link: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i
#### Difficulty: <span style="color:#ffb800">Medium</span>  
#### Topics: Array, Bit Manipulation, Queue, Sliding Window, Prefix Sum

---
## Description  
You are given a binary array `nums`.

You can do the following operation on the array **any** number of times (possibly zero):

- Choose **any** 3 **consecutive** elements from the array and **flip all** of them.  

**Flipping** an element means changing its value from 0 to 1, and from 1 to 0.

Return the **minimum** number of operations required to make all elements in `nums` equal to 1. If it is impossible, return -1.


**Example 1:**
<pre>
<b>Input:</b> nums = [0,1,1,1,0,0]
<b>Output:</b> 3
<b>Explanation:</b>
We can do the following operations:
    - Choose the elements at indices 0, 1 and 2. The resulting array is <code>nums = [<u>1,0,0</u>,1,0,0]</code>.
    - Choose the elements at indices 1, 2 and 3. The resulting array is <code>nums = [1,<u>1,1,0</u>,0,0]</code>.
    - Choose the elements at indices 3, 4 and 5. The resulting array is <code>nums = [1,1,1,<u>1,1,1</u>]</code>.
</pre>

**Example 2:**
<pre>
<b>Input:</b> nums = [0,1,1,1]
<b>Output:</b> -1
<b>Explanation:</b>
It is impossible to make all elements equal to 1.
</pre>
 

**Constraints:**

- <code>3 <= nums.length <= 10<sup>5</sup></code>
- `0 <= nums[i] <= 1`


<details>
    <summary><b>Hint</b></summary>
    <ul>
        <li>If <code>nums[0]</code> is 0, then the only way to change it to 1 is by doing operation on the first 3 elements of the array</li>
        <li>After changing <code>nums[0]</code> to 1, use the same logic on the remaining array.</li>
    </ul>
</details>

---
## Approach
1. **Iterate through the array:** Start from the first element and iterate through the array.
2. **Check for zeros:** If the current element is 0:  
    - If it is the second last element, return -1 as it is impossible to flip it (only two elements left).
    - If it is not the second last or last element, flip the current element and the next two elements (i.e., `nums[i]`, `nums[i+1]`, and `nums[i+2]`). Count this as one operation.
3. **Return the operation count:** After iterating through the array, return the total number of operations performed.

---
## Code

**Time Complexity:** O(n), where n is the length of the array.  
**Space Complexity:** O(1), as we are using a constant amount of space.

**C++ Code:**
```c++
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size(), count = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                if (i + 2 >= n) return -1;
                nums[i + 1] = 1 - nums[i + 1];
                nums[i + 2] = 1 - nums[i + 2];
                count++;
            }
        }

        return count;
    }
};