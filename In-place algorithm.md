# In-place algorithm

An **in-place algorithm** is an algorithm that transforms data using a constant amount of extra space. In other words, it **modifies the input directly** without requiring significant additional memory for a copy of the data structure.

---

## 🔍 Key Characteristics
- **Constant auxiliary space**: Typically uses **O(1)** or **constant extra memory**.
- **Modifies input**: Operates on the input data structure directly.
- **Efficient in memory**: Ideal for memory-constrained environments.

---

## 🛠️ Examples: In-Place Reveral of an Array
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