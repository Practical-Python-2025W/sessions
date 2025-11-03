def f(n, mem={0:1, 1:1, 2:2, 3:6}):
    """Compute factorial of n using memoization."""
    if n not in mem:
        prev_number = n - 1
        prev_fact = f(prev_number)
        mem[n] = n * prev_fact
    return mem[n]

f(10)