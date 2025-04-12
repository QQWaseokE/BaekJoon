#include <stdio.h>

int main(void)
{
    int a, b;

    scanf("%d", &a);
    getchar();
    scanf("%d", &b);

    if (a>0) {
        if (b>0) {
            printf("1");
        }
        else if (b<0) {
            printf("4");
        }
    }
    if (a<0) {
        if (b>0) {
            printf("2");
        }
        else if (b<0) {
            printf("3");
        }
    }

    return 0;
}