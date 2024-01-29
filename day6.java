import java.util.Scanner;

public class SubstringExample {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the input string
        String s = scanner.nextLine();

        // Read the indices
        int start = scanner.nextInt();
        int end = scanner.nextInt();

        // Print the substring
        String result = s.substring(start, end);
        System.out.println(result);

        scanner.close();
    }
}
