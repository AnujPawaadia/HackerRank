
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int n,i,sum=0;
    int *arra;
    scanf("%d",&n);
    arra=(int*)malloc(n*sizeof(int));
    for(i=0; i<n; i++)
    {
        scanf("%d",&arra[i]);

    }
    for(i=n-1;i>=0;i--)
    {
        printf("%d ",arra[i]);
    }

    return 0;
}
