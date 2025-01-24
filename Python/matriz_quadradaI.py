def ordem():
    try:
        while True:
            n=int(input())
            m=[0]*n
            m[0]=1
            m[n-1]=2
            for w in range(0,n,1):
                if w > 0 and w < n-1:
                     m[w] = 3
            troca(m,n)
    except EOFError:
        print(end="")

def troca(m,n):
    n=n-1
    for x in range(0,n+1,1):
        print(m[x],end="")
    print()
    for w in range(0,n,1):
        x=m[w]
        y=m[n-w]

        if m[w] < m[w+1]:
            m[w] = m[w+1]
            m[w+1]=x

        if m[n-w] < m[n-(w+1)] or m[n-w] > m[n-(w+1)]  :
            m[n-w] = m[n-(w+1)]
            m[n-(w+1)]=y
        if m[n-w] == m[n-(w+1)]:
            m[n-w] = 1
        for e in range(0,n+1,1):
            print(m[e],end="")
        print()

ordem()

