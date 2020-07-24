def isdivisiblebyanother(n):
    i=3
    while n>=i :
        if n%i == 0:
            return i
        i+=2
    return 0

def solution(n1):
    n = int(n1)
    count =0
    while(n>1):
        if n%2 == 0:
            n = n/2
            count +=1
        else:
            a = isdivisiblebyanother(n+1)
            b = isdivisiblebyanother(n-1)
            if a ==0 and b == 0:
                n = (n-1)/2
                count +=2
            elif a==0 and b != 0:
                n = (n+1)/2
                count+=2
            elif a != 0 and b == 0:
                n = (n-1)/2
                count +=2
            elif a != 0 and b != 0:
                if(a>=b):
                    n = (n-1)/2
                    count += 2
                else:
                    n = (n+1)/2
                    count += 2
    return count

s = solution("52")
print(s)


       ## great solution ###

def solution(x):
  counter = 0
  x = int(x)
  while x > 1:
    if x%2 == 0:
      x=x//2
    elif x==3 or x%4 == 1:
      x-=1
    else:
      x+=1
    counter +=1
  return int(counter)