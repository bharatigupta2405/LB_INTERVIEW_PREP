def maxmin(a):
    a.sort()
    m={a[0],a[len(a)-1]}
    return m

j=input('Enter an array')
print(maxmin(j))