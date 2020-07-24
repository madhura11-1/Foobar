int a = 10;
int b = 2;

ans = 0;

while(min(a,b)!=1):
    if a==b:
        print("impossible")
    elif a>b:
        k = a/b-1
        if k!=0:
            a=a-b*k
            ans+=k
        else:
            a=a-b
            ans+=1
    else:
        k = b/a-1
        if k!=0:
            b=b-a*k
            ans+=k
        else:
            b=b-a
            ans+=1
print(ans+max(a,b)-1)