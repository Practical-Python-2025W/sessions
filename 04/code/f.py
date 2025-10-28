def f(n, mem={0:1, 1:1, 2:2, 3:6}):
    if n not in mem:
        mem[n] = n * f(n-1, mem)
    return mem[n]

