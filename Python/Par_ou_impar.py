n = int(input())

for w in range(1,n+1,1):
    x = int(input())
    if x % 2 == 0 and x > 0:
        print("EVEN POSITIVE")
    elif x % 2 == 0 and x < 0:
        print("EVEN NEGATIVE")
    if x % 2 == 1 and x > 0:
        print("ODD POSITIVE")
    elif x % 2 == 1 and x < 0:
        print("ODD NEGATIVE")
    if x == 0:
        print("NULL")
