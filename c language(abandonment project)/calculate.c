#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b, c, d, e;
    float f;
    int max;

    printf("input 2 data: ");
    scanf("%d %d", &a, &b);

    c = a + b;
    d = a - b;
    e = a * b;
    f = (float)a / b;
    
    if( b < a)
    {
        max = a;
    }
    else
    {
        max = b;
    }

    printf("%d + %d = %d\n", a, b, c);
    printf("%d - %d = %d\n", a, b, d);
    printf("%d * %d = %d\n", a, b, e);
    printf("%d / %d = %f\n", a, b, f);
    printf("max = %d\n", max);
    scanf("확인", &a);
    return 0;
}