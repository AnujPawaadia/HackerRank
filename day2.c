#include <stdio.h>

int main() {
    int num, sum = 0;

    // Input
    scanf("%d", &num);

    // Calculate the sum of digits
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }

    // Output
    printf("%d\n", sum);

    return 0;
}
