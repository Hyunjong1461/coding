#include <stdio.h>

int main(void)
{
	int a = 20;
	int b = 30;
	float p = 3.14000;
	float q = 4.20000;
	float m = 7.23000;
	float n = 1.2;

	printf("\tb/a -> %d\n", b / a);
	printf("\tb/a -> %f\n", b / a);
	printf("\tp-q -> %f\n", p-q);
	printf("\tm*n -> %lf\n", m*n);

	return 0;
}