import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

public class RegexValidator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int testCases = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character after reading the number of test cases

        for (int i = 0; i < testCases; i++) {
            String pattern = scanner.nextLine();
            if (isValidRegex(pattern)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }

        scanner.close();
    }

    private static boolean isValidRegex(String pattern) {
        try {
            // Attempt to compile the regex pattern
            Pattern.compile(pattern);
            return true; // If compilation succeeds, the pattern is valid
        } catch (PatternSyntaxException e) {
            return false; // If compilation fails, the pattern is invalid
        }
    }
}
