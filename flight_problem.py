n,m = tuple(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
if(b[0]<a[0]):
    print(-1)
else:
    i = 0
    j = 0 
    cc = 0
    time = 1
    while(i<n):
        while(b[j]<a[i]): 
            i+=1
        cc+=1
        i+=1
        j+=1
        print(cc,i,j)
        if j>m-1:
            print("----------")
            time = 1+(n-cc)*2
            break
        elif j==m-1 and i>n-1:
            time = 1+(n-cc)*2
            break
    print(time)



