#include <stdio.h>

int main(void)
{
    int a, b, c, d;

    scanf("%d", &a);
    getchar();
    scanf("%d", &b);
    getchar();
    scanf("%d", &c);

    if (a == b && b == c) {
        d = 10000 + a * 1000;
        printf("%d", d);
    }
    else if (a==b && b != c) {
        d = 1000 + a * 100;
        printf("%d", d);
    }
    else if (b==c && c != a) {
        d = 1000 + b * 100;
        printf("%d", d);
    }
    else if (a==c && c != b) {
        d = 1000 + a * 100;
        printf("%d", d);
    }
    else {
        if (a>b && a>c) {
            d = a * 100;
            printf("%d", d);
        }
        if (b>a && b>c) {
            d = b * 100;
            printf("%d", d);
        }
        if (c>b && c>a) {
            d = c * 100;
            printf("%d", d);
        }
    }
    return 0;
}