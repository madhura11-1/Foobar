import java.math.BigInteger;
public class Solution {
    public static String solution(String x, String y) {
        BigInteger l = new BigInteger(x);
        BigInteger r = new BigInteger(y);
        BigInteger one = new BigInteger("1");
        BigInteger zero = new BigInteger("0");
        BigInteger oneminus = new BigInteger("-1");
        BigInteger cycles = new BigInteger("0");
        long p = -1;
        if(l.equals(one) && r.equals(one))
         return "0";
        else{
            while(l.compareTo(zero) >= 0 && r.compareTo(zero) >= 0){
                 if(r.compareTo(l) > 0)
                  r = r.subtract(l);
                 else
                  l = l.subtract(r);
                  cycles = cycles.add(BigInteger.ONE);
               if(l.equals(one) && r.equals(one)){
                    break;
                }
                if(l.compareTo(zero) <= 0 || r.compareTo(zero) <= 0){
                    cycles = BigInteger.valueOf(p);
                    break;
                }
            }
            
            if(cycles.equals(oneminus))
            return "impossible";
            else{
                String m = cycles.toString();
                return m;
            }
        }
        
        
    }
}