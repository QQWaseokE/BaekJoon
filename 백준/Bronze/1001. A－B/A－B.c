#include <stdio.h>

int main(void)
{
    int a, b, c;

    scanf("%d", &a);
    getchar();
    scanf("%d", &b);

    c = a - b;
    printf("%d", c);

    return 0;
}