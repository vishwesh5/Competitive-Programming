def ab_n(n):
    if n==0:
        return (1,0)
    else:
        ab_n_1 = ab_n(n-1)
        b_n_1 = ab_n_1[1]
        a_n_1 = ab_n_1[0]
        a_n = b_n_1
        b_n = a_n_1 + b_n_1
        return (a_n,b_n)

n = int(input().strip())
print(" ".join(list(map(str,list(ab_n(n))))))
