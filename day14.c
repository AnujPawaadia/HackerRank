#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char str[1000] = "";
    scanf("%s", str);
    
    int freq[10] = {0};
    
    for(int i = 0; i < strlen(str); i++)
    {
        int temp = str[i] - '0';
        // If temp is between 0-9 we're in bounds for our freq arr
        if ((temp>=0) && (temp<=9))
        {
            freq[temp]++;            
        }
    }
    
    for (int i = 0; i<10;i++)
    {
        printf("%d ", freq[i]);
    }
    
    return 0;
}
