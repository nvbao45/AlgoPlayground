# Difference Array | Range update query in O(1)

A difference array is a technique used in computer science to efficiently perform range update operations on an array. Here's a breakdown of the concept.

**Core Idea**  
- Instead of directly updating every element within a specified range, a difference array tracks the *differences* between consecutive elements of the original array.
- This allows range updates to be performed with a small of operations, typically just two.
- The original array can then be reconstructed from the difference array by calculating a prefix sum.

**How It Works**
1. Creating the Difference Array:
    - Given an array `A`, the difference array `D` is created as follows:
        - `D[0] = A[0]`
        - `D[i] = A[i] - A[i-1]` for `i > 0`
2. Range Updates:
    - To add a value `val` to all elements in the range `[left, right]` of the original array `A`:
        - Add `val` to `D[left]`.
        - Subtract `val` from `D[right + 1]` (if `right + 1` is within the array bounds).
3. Reconstructing the Original Array:
    - The original array `A` can be reconstructed from the difference array `D` by calculating the prefix sum of `D`:
        - `A[0] = D[0]`
        - `A[i] = A[i-1] + D[i]`

**Use Cases**
- Efficient Range Updates:
    - Difference arrays are particularly useful when you need to perform many range update operations on a large array.
- Event Counting in Time Intervals:
    - They can be used to track the number of events occurring af different points in time.
- Competitive Programming:
    - Difference arrays are a common technique in competitive programming problems that involve range updates.
 
**Key Advantages**
- Improved Time Complexity
    - Range updates can be performed in constant time, O(1), instead of linear time, O(n).
-Efficiency:
    - They provide a more efficient way to handle multiple range updates.
