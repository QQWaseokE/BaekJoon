#include <stdio.h>

int main(void)
{
    int a, b;

    scanf("%d", &a);
    getchar();
    scanf("%d", &b);

    if (a>b) {
        printf(">");
    }
    if (a<b) {
        printf("<");
    }
    if (a==b) {
        printf("==");
    }

    return 0;
}