#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);

    if (a>b) {
        if (a%b == 0){
            printf("multiple");
            printf("\n");
        }
        else {
            printf("neither");
            printf("\n");
        }
    }
    else if (a<b) {
        if (b%a == 0){
            printf("factor");
            printf("\n");
        }
        else {
            printf("neither");
            printf("\n");
        }
    }

    while(a != 0 && b!= 0) {
        scanf("%d %d", &a, &b);

        if (a>b) {
            if (a%b == 0){
                printf("multiple");
                printf("\n");
            }
            else {
                printf("neither");
                printf("\n");
            }
        }
        else if (a<b) {
            if (b%a == 0){
                printf("factor");
                printf("\n");
            }
            else {
                printf("neither");
                printf("\n");
            }
        }
    }


    return 0;
}