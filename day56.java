import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

 public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        String [] pair_left = new String[t];
        String [] pair_right = new String[t];
        
        for (int i = 0; i < t; i++) {
            pair_left[i] = s.next();
            pair_right[i] = s.next();
        }
HashSet<String>set=new HashSet<String>();
        int count=0;
        for(int i=0,j=0;i<pair_left.length&&j<pair_right.length;i++,j++)
        {
            if(set.contains(pair_left[i]+" "+pair_right[j]))
            {
                System.out.println(count);
            }
            else
            {
            set.add(pair_left[i]+" "+pair_right[j]);
            System.out.println(++count);
            }  
            
        }    



    }
}
