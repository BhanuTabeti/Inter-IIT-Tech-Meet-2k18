#include <stdio.h>

int main(int argc, char const *argv[])
{
	printf("[");
	for (int i = 0; i < 50; ++i)
	{
		printf("0, ");
	}
	for (int i = 0; i < 50; ++i)
	{
		printf("1, ");
	}
	printf("]\n");
	return 0;
}