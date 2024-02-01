#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    // Dynamically allocate memory for the array
    int *arr = (int*)malloc(n * sizeof(int));

    // Check if memory allocation was successful
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;  // Exit with an error code
    }

    // Input values into the dynamically allocated array
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Calculate the sum of elements in the array
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
