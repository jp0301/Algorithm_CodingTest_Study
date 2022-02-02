#include <stdio.h>

int main(void) {
    int n;
    int m;
    scanf("%d %d", &n, &m);
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; i < m; i++) {
            printf("%d", "*");
        }
    }
    
    return 0;
}