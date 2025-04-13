# ⚡ Fast Exponentiation Algorithm

The **Fast Exponentiation Algorithm**, also known as **Exponentiation by Squaring**, is an efficient method to compute <code>a<sup>n</sup></code> (`a` raised to the power of `n`), especially when `n` is a large number.

---

### ❌ Naive Approach:
Multiplying `a` by itself `n` times takes **O(n)** time, which becomes inefficient for large exponents.

---

### ✅ Fast Exponentiation:
This algorithm reduces the time complexity to **O(log n)** by using the following observations:

- If `n` is **even**, then:
<code>
    a<sup>n</sup>=(a<sup>n/2</sup>)<sup>2</sup>
</code>

- If `n` is **odd**, then:
<code>
    a<sup>n</sup>=a*(a<sup>(n-1)/2</sup>)<sup>2</sup>
</code>

This method repeatedly squares the base and reduces the exponent by half in each step, making it logarithmically faster.


## 🔢 Recursive Version (Python)
```python
def fast_power(a, n):
    if n == 0:
        return 1
    half = fast_power(a, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return a * half * half
```

## 🔁 Iterative Version (Python)
```python
def fast_power_iterative(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a *= a
        n //= 2
    return result
```

## 💡 With Modulo
```python
def fast_power_mod(a, n, mod):
    result = 1
    a = a % mod
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        n //= 2
    return result
```

## 🎯 Example
### ⚡ Fast Exponentiation with Modulo

Compute <code>3<sup>13</sup> % 100</code>

### 👀 Step-by-Step Execution of <code>3<sup>13</sup> % 100</code>

1. **Initial values:**  
   - `a = 3`, `n = 13`, `mod = 100`  
   - `result = 1`

---

2. **Iteration 1:**  
   - `n = 13` (odd) → `result = result * a % mod = 1 * 3 % 100 = 3`  
   - Update `a = a * a % mod = 3 * 3 % 100 = 9`  
   - Update `n = n // 2 = 6`

---

3. **Iteration 2:**  
   - `n = 6` (even) → skip result update  
   - Update `a = a * a % mod = 9 * 9 % 100 = 81`  
   - Update `n = n // 2 = 3`

---

4. **Iteration 3:**  
   - `n = 3` (odd) → `result = result * a % mod = 3 * 81 % 100 = 43`  
   - Update `a = a * a % mod = 81 * 81 % 100 = 61`  
   - Update `n = n // 2 = 1`

---

5. **Iteration 4:**  
   - `n = 1` (odd) → `result = result * a % mod = 43 * 61 % 100 = 23`  
   - Update `a = a * a % mod = 61 * 61 % 100 = 21`  
   - Update `n = n // 2 = 0`

---

6. **Loop ends (n = 0)**  
   ✅ Final `result = 23`

---
