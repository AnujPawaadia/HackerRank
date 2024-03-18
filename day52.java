import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

/**
 *
 * @author Thinh_Nguyen
 */
public class javaanhlocday 
{   
    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        String n=sc.nextLine();
        BigInteger bg=new BigInteger(n);
        if(bg.isProbablePrime(1)==true)
            System.out.println("prime");
        else
            System.out.println("not prime");
    
    }
}
