import java.util.Scanner;

public class Solution {


public static String getSmallestAndLargest(String s, int k) {
      String smallest = s.substring(0, k);
    String largest = s.substring(0, k);

    for(int i=0;i<=s.length()-k;i++){
      String l= s.substring(i,i+k);
      largest =largest.compareTo(l)<0?l:largest;
      smallest =l.compareTo(smallest)<0?l:smallest;
    }


    return smallest + "\n" + largest;
}



    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
