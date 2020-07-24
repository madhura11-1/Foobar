import numpy as np 
from fractions import Fraction
def solution(m):
        notzero = 0
        sumi = 0
        row_notzero = []
        row_zero = []
        sum_row = {}

        
        for i in range(0, len(m)):
            sumi = 0
            notzero = 0
            for j in range(0,len(m)):
                if m[i][j] != 0 :
                    notzero = 1
                    sumi = sumi +m[i][j]
            if sumi != 0 :
                sum_row[i] = sumi
            if notzero == 1 :
                row_notzero.append(i)
            else:
              row_zero.append(i)

        q = []
        result = []
        sum2 = 0  
        numerator = []
        denominator = []
        maximum = 0
        
        for k in range(0,len(row_notzero)):
            a = []
            for h in range(0,len(row_notzero)):
                if k == h :
                    sum_row1 = sum_row.get(row_notzero[k])
                    a.append(1 -((m[row_notzero[k]][row_notzero[h]])/sum_row1))
                else :
                    a.append(-m[row_notzero[k]][row_notzero[h]]/sum_row1)
            q.append(a) 
            
        y = np.linalg.inv(q)
        mat=[]
        for dhur in range(0,len(row_notzero)):
          f=[]
          for div in range(0,len(row_zero)):
            f.append(m[row_notzero[dhur]][row_zero[div]]/sum_row.get(dhur))
          mat.append(f)

        prod=np.dot(y,mat)
        for z in range(0,len(prod[0])):
            numerator.append(Fraction(prod[0][z]).limit_denominator().numerator)
            denominator.append(Fraction(prod[0][z]).limit_denominator().denominator)
            
        maximum = max(denominator)
        
        for o in range(0,len(denominator)):
            denominator[o] = maximum/denominator[o]
            numerator[o] = int(numerator[o]*denominator[o])
        numerator.append(int(maximum))        
        
        return numerator 
