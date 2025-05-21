# In-place algorithm

An **in-place algorithm** is an algorithm that transforms data using a constant amount of extra space. In other words, it **modifies the input directly** without requiring significant additional memory for a copy of the data structure.

---

## 🔍 Key Characteristics
- **Constant auxiliary space**: Typically uses **O(1)** or **constant extra memory**.
- **Modifies input**: Operates on the input data structure directly.
- **Efficient in memory**: Ideal for memory-constrained environments.

---

## 🛠️ Examples: In-Place Reveral of an Array

Given an array, `a` of _n_ items, suppose we want an array that holds the same elements in reversed order and to dispose of the original. One seemingly simple way to to this is to create a new array of euqal size, fill it with copies from `a` in the appropriate order and then delete `a`.

<pre>
<span style="color: blue; font-weight: bold;">function</span> reverse(a[0..n - 1])
    <span style="color: green;">allocate</span> b[0..n - 1]
    <span style="color: blue; font-weight: bold;">for</span> i <span style="color: blue; font-weight: bold;">from</span> 0 <span style="color: blue; font-weight: bold;">to</span> n - 1
        b[i] = a[n - i - 1]
    <span style="color: blue; font-weight: bold;">return</span> b
</pre>

Unfortunately, this requires _O(n)_ extra space for having the arrays `a` and `b` available simultaneously. Also, allocation and deallocation are often slow operations. Since we no longer need `a`, we can instead overwrite it with its own reversal using this in-place algorithm which will only need constant number (2) of integers for the auxiliary veriables `i` and `tmp`, no matter how large the array is.

<pre>
<span style="color: blue; font-weight: bold;">function</span> reverse(a[0..n - 1])
    <span style="color: blue; font-weight: bold;">for</span> i <span style="color: blue; font-weight: bold;">from</span> 0 <span style="color: blue; font-weight: bold;">to</span> floor((n-2)/2)
        tmp := a[i]
        a[i] := a[n - i - 1]
        a[n - i - 1] := tmp
</pre>


### C++ Implementation
```cpp
void reverse_array(int arr[], int n) {
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - i - 1];
        arr[n - i - 1] = temp;
    }
}
```

### Python Implementation
```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

---

## 🧠 Common In-Place Algorithms
- Bubble Sort
- Selection Sort
- Quick Sort (in-place partitioning)
- Reversing a linked list
- Rotating an array