import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        ArrayList<Integer> ar=new ArrayList<Integer>();
        for(int i=0;i<a;i++)
        {
            ar.add(sc.nextInt());
        }
        
        int n=sc.nextInt();
        int index;
        int number;
        String s;
        for(int j=0;j<n;j++)
        {
            s=sc.next();
            
            
            if(s.equalsIgnoreCase("Insert"))
            {
                index=sc.nextInt();
                number=sc.nextInt();
                ar.add(index,number);
            }
            else if(s.equalsIgnoreCase("Delete"))
            {
                index=sc.nextInt();
            
                ar.remove(index);
            }
            else
            {
                System.out.println("error");
            }
        }
        for (int z : ar) { 
            System.out.print(z + " "); 
        } 
        
    }
}
