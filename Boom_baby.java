public class Solution {
    public static String solution(String x, String y) {
        long l = Long.parseLong(x);
        long r = Long.parseLong(y);
        long cycles = 0;
        if(l == 1 && r == 1)
         return "0";
        else{
            while(l >= 0 && r >= 0){
                 if(l<r)
                  r = r-l;
                 else
                  l = l-r;
                  cycles++;
               if(l == 1 && r == 1){
                    break;
                }
                if(l <= 0 || r <= 0){
                    cycles = -1;
                    break;
                }
            }
            
            if(cycles == -1)
            return "impossible";
            else{
                String m =Long.toString(cycles);
                return m;
            }
        }
        
        
    }
}