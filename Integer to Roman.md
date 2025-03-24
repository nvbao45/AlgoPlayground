Seven different symbols represent Roman numerals with the following values:

|Symbol|Value |
|------|------|
|I     |1     |
|V     |5     |
|X     |10    |
|L     |50    |
|C     |100   |
|D     |500   |
|M     |1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Conventing a decimal place value into a Roman numeral has the following rules:
- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtact its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the **subtractive form** representing one symbol subtracted from the following symbol, for example, 4 is 1 (`I`) less than 5 (`V`): `IV` and 9 is 1 (`I`) less than 10 (`X`): `IX`. Only the following subtractive forms are used: 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`), and 900 (`CM`).
- Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiples times. If you need to append a symbol 4 times use the subtractive form.

Given an interger, convert it to a Roman numeral.

**Example 1:**
<pre>
<b>Input:</b> num = 3749
<b>Output:</b> "MMMDCCXLIX"
<b>Explanation:</b> 
3749 = 3 * 1000 + 7 * 100 + 4 * 10 + 9
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C) + 100 (C)
  40 = XL as 50 (L) - 10 (X)
   9 = IX as 10 (X) - 1 (I)
Note: 49 is not 1 (I) less than 50 (L) because the conversion is based on decimal places.
</pre>

**Example 2:**
<pre>
<b>Input:</b> num = 58
<b>Output:</b> "LVIII"
<b>Explanation:</b>
58 = 5 * 10 + 8
50 = L as 50 (L)
 8 = VIII as 5 (V) + 1 (I) + 1 (I) + 1 (I)
</pre> 

**Example 3:**
<pre>
<b>Input:</b> num = 1994
<b>Output:</b> "MCMXCIV"
<b>Explanation:</b>
1994 = 1 * 1000 + 9 * 100 + 90 + 4
1000 = M as 1000 (M)
 900 = CM as 1000 (M) - 100 (C)
  90 = XC as 100 (C) - 10 (X)
   4 = IV as 5 (V) - 1 (I)
</pre>

**Constraints:**
- <code>1 <= num <= 3999</code>

---
**Solution**
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # Convert an integer to a Roman numeral.
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        result = []
        # Iterate through the list of Roman numerals and their values.
        for value, numeral in roman_numerals:
            # While the current number is greater than or equal to the value,
            # append the corresponding numeral to the result and subtract the value from the number.
            while num >= value:
                result.append(numeral)
                num -= value

        return ''.join(result)
```