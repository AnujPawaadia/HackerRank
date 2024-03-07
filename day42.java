import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        int negative_count = 0;
        Scanner scan = new Scanner(System.in);
        int arraySize = scan.nextInt();
        
        int[] currentSums = new int[arraySize];
        for (int n=1; n <= arraySize; ++n){
            int value = scan.nextInt();
             for (int i=0; i <n; ++i){
                 currentSums[i]+=value;
                 if (currentSums[i] < 0) negative_count++;
             }
        }
        System.out.println(negative_count);
        
    }
}
