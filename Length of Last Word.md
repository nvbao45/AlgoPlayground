# LeetCode 58. Length of Last Word
#### Problem Link: https://leetcode.com/problems/length-of-last-word
#### Difficulty: <span style="color:#1cb8b8">Easy</span>  
#### Topics: String

---
## Description  

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string.

A **word** is a maximal substring consisting of non-space characters only.

***Example 1:**
<pre>
<b>Input:</b> s = "Hello World"
<b>Output:</b> 5
<b>Explanation:</b> The last word is "World" with length 5.
</pre>

**Example 2:**
<pre>
<b>Input:</b> s = "   fly me   to   the moon  "
<b>Output:</b> 4
<b>Explanation:</b> The last word is "moon" with length 4.
</pre>

**Example 3:**
<pre>
<b>Input:</b> s = "luffy is still joyboy"
<b>Output:</b> 6
<b>Explanation:</b> The last word is "joyboy" with length 6.
</pre>

**Constraints:**
- <code>1 <= s.length <= 10<sup>4</sup></code>
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

---
## Approach
1. Initialize a variable `length` to 0 to keep track of the length of the last word.
2. Iterate through the string `s` from the end to the beginning.
3. For each character, check if it is not a space:
   - If it is not a space, increment the `length` variable.
   - If it is a space and `length` is greater than 0, break the loop as we have found the last word.
4. Return the value of `length` as the result.

---
## Code

**Time Complexity:** O(n), where n is the length of the string `s`.  
**Space Complexity:** O(1), as we are using a constant amount of space.

**C++ Code:**
```c++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] != ' ') {
                ++length;
            } else if (length > 0) {
                break;
            }
        }
        return length;
    }
};
```