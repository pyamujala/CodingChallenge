a = ['a', 'b', 'c']

def quickperm(a):
    N = len(a)
    p = [*range(N+1)]
    i = 1
    while True:
        yield a
        if i >= N: break

        p[i] = p[i] - 1
        j = 0 if i % 2 == 0 else p[i]
        a[j], a[i] = a[i], a[j]

        i = 1
        while p[i] == 0:
            p[i] = i
            i += 1

for i in quickperm(a):
    print(i)