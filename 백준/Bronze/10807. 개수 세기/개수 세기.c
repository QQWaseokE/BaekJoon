#include <stdio.h>

int main(void)
{
    int n, x, count;
    count =0;

    scanf("%d", &n);
    
    int arr[n];

    for (int i=0;i<n;i++) {
        scanf("%d", &arr[i]);
    }

    scanf("%d", &x);

    for (int i=0;i<n;i++) {
        if (arr[i] == x) {
            count += 1;
        }
    }

    printf("%d", count);

    return 0;
}