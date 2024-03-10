
import java.util.*;
import java.util.regex.*;
import java.io.*;

public class Solution{
    public static void main(String []argh)
    {HashMap<String,Integer> phone_Book=new HashMap<>();
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        sc.nextLine();
        for (int i=0;i<n;i++){
            String name=sc.nextLine();
            Integer Number=sc.nextInt();
            sc.nextLine();
            if (name.equals(name.toLowerCase()) && Number.toString().matches("[1-9]+"));
            {phone_Book.put(name,Number);}
        }
        while (sc.hasNext()){
            String wanted=sc.nextLine();
            if(phone_Book.containsKey(wanted)){
                System.out.println(wanted+"="+phone_Book.get(wanted));
            }else{
                System.out.println("Not found");
            }
        }
    }//main
}//Main
