#include <stdio.h>
#define PHI 3.14
#define CIRCUM(x) 2*x*PHI
#define AREA(x) x**2*PHI

int main(void)
{
    printf("%f", CIRCUM(2));
    printf("%f", AREA(2));

    return 0;
    
}