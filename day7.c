#include <stdio.h>
#include <stdlib.h>

int main() {
    // Input size of the array
    int n;
    scanf("%d", &n);

    // Dynamically allocate memory for the array
    int *arr = (int*)malloc(n * sizeof(int));

    // Input array elements
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Calculate the sum of array elements
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    // Print the sum
    printf("%d\n", sum);

    // Free the dynamically allocated memory
    free(arr);

    return 0;
}
