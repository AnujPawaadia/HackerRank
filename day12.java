import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Convert the strings to lowercase for case-insensitivity
        a = a.toLowerCase();
        b = b.toLowerCase();

        // Check if the lengths are equal
        if (a.length() != b.length()) {
            return false;
        }

        // Check character counts using Scanner
        Scanner scannerA = new Scanner(a);
        Scanner scannerB = new Scanner(b);

        while (scannerA.hasNext()) {
            char currentChar = scannerA.next().charAt(0);
            int countA = a.length() - a.replace(String.valueOf(currentChar), "").length();
            int countB = b.length() - b.replace(String.valueOf(currentChar), "").length();

            if (countA != countB) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
