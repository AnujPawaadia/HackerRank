#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int andm=0,orm=0,exorm=0,a,b,c;
  for (int i=1; i<=n; i++) {
      for(int j=i+1; j<=n; j++){
          a = i&j;
          b = i|j;
          c = i^j;
          if(a>andm && a<k){
              andm=a;
          }
          if(b>orm && b<k){
              orm=b;
          }
          if(c>exorm && c<k){
              exorm=c;
          }
      }
  }
  printf("%d\n%d\n%d", andm, orm, exorm);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
