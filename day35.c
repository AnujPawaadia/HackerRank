#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getDistinctCharCount(const char* a) {
    int sumi=0;
    int stra[26];
    int size=strlen(a);
    for(int i=0;i<26;i++) {
        stra[i]=0;
    }
    for(int i=0;i<size;i++) {
        int asci=(int)a[i];
        stra[asci-97]=1;
    }
    for(int i=0;i<26;i++) {
        sumi+=stra[i];
    }
    return sumi;
}

int lexicographic_sort(const char* a,const char* b) {
    if(strcmp(a,b)<=0) {
        return 0;
    } else {
        return 1;
    }
}

int lexicographic_sort_reverse(const char* a,const char* b) {
    if(strcmp(b,a)<=0) {
        return 0;
    } else {
        return 1;
    }
}

int sort_by_number_of_distinct_characters(const char* a,const char* b) {
    int disa=getDistinctCharCount(a);
    int disb=getDistinctCharCount(b);
    if(disa<disb) {
        return 0;
    } else if(disa==disb) {
        return lexicographic_sort(a,b);
    } else {
        return 1;
    }
}

int sort_by_length(const char* a,const char* b) {
    int siza=strlen(a);
    int sizb=strlen(b);
    if(siza<sizb) {
        return 0;
    } else if(siza==sizb) {
        return lexicographic_sort(a,b);
    } else {
        return 1;
    }
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a,const char* b)) {
    for(int i=0;i<len;i++) {
        for(int j=0;j<len;j++) {
            if(cmp_func(arr[j],arr[i])==1) {
                char* temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
}

int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}
