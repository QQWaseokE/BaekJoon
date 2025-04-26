#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    char n[1000];
    int b, ans = 0;

    scanf("%s %d", n, &b);

    int len = strlen(n);

    for (int i=0;i<len;i++) {
        if (n[i] >= 'A' && n[i] <= 'Z') {

            int num = n[i] - 'A' + 10;
            ans += num * pow(b,strlen(n) - i - 1);
        }
        else {
            int num = n[i] - '0';
            ans += num * pow(b,strlen(n) - i - 1);
        }
    }
    printf("%d", ans);


    return 0;
}