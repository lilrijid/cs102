values=input()
n=input()


def group(values, n):
    
    
    m = n*n
    a = []
    b = []
    for element in values:
        for element in range(n):
            a = a.append(element)
        while n+n<m:
            for element in range(n,n+n):
                b = b.append(element)
                a = zip(a,b)
                n+=n
    return a
text = group(values, n)
print (text)
