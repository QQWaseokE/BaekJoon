#include <stdio.h>

int main(void)
{
    int n, m;
    scanf("%d %d", &n, &m);
    int Arr1[n][m];
    int Arr2[n][m];
    int result[n][m];

    for (int i=0;i<n;i++) {
        for (int j=0;j<m;j++) {
            scanf("%d", &Arr1[i][j]);
        }
    }

    for (int i=0;i<n;i++) {
        for (int j=0;j<m;j++) {
            scanf("%d", &Arr2[i][j]);
        }
    }

    for (int i=0;i<n;i++) {
        for (int j=0;j<m;j++) {
            printf("%d ", result[i][j] = Arr1[i][j] + Arr2[i][j]);
        }
        printf("\n");
    }


    return 0;
}