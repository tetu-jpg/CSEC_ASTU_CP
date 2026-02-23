n, h=map(int,input().split())
heights=list(map(int,input().split()))
total=0
for height in heights:
    if height<=h:
        total=total+1
    else:
        total=total+2
print(total)
