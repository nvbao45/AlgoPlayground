Given an array of strings `words` and a width `maxWith`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.  
  
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra space `' '` when necessary so that each line has exactly `maxWidth` characters.  
  
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.  
  
For the last line of text, it should be left-justified, and no extra space is inserted between words.  

**Note:**
- A word is defined as a character sequence consisting of non-space characters only.
- Each world's length is guaranteed to be greater than `0` and not exceed `maxWidth`.
- The input array `words` contains at least one word.

**Example 1:**
<pre>
<b>Input:</b> words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
<b>Output:</b> 
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
</pre>

**Example 2:**
<pre>
<b>Input:</b> words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
<b>Output:</b> 
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
<b>Explanation:</b> Note that the last line is "shall be        " instead of "shall         be", because the last line must be left-justified instead of fully justified.
Note that the second line is also left-justified because it contains only one word.
</pre>

**Example 3:**
<pre>
<b>Input:</b> words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
<b>Output:</b> 
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer. Art is",
  "everything  else  we",
  "do                  "
]
</pre>
  
---
**Solutions**
```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        num_of_letters = 0

        for w in words:
            # Check if adding the next word exceeds the maxWidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                # Join the words and add to result
                res.append(''.join(cur))
                # Reset current line and letter count
                cur, num_of_letters = [], 0
            # Add the current word to the line
            cur += [w]
            # Update the number of letters in the current line
            num_of_letters += len(w)
        
        # Join the last line and add to result
        return res + [' '.join(cur).ljust(maxWidth)]
```