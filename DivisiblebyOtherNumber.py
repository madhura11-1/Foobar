def isdivisiblebyanother(n):
    i=3
    while n>=i :
        if n%i == 0:
            return i
        i+=2
    return 0   

def solution(n1):
    n = int(n1)
    count = 0
    while(n > 1):
        if n%2 == 0:
            n = n/2
            count+=1
        else:
            if(isdivisiblebyanother(n-1)):
                n = (n+1)/2
                count += 2
            else:
                n = (n-1)/2
                count+=2
                     
    return count   
s = solution("52")   
print(s)


                
    # Your code here