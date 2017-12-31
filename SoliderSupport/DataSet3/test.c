#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	char name[300],test[50];
	scanf("%s",name);
	// printf("hi\n");
	FILE *f = fopen(name,"r");
	int temp = 0,lineno = 0;
	while(!feof(f)){
		fscanf(f,"%s",test);
		temp++;
		if (test[strlen(test) - 2] == ']')
		{
			lineno++;
			if (temp < 17)
			{
				printf("Line Number : %d\n",lineno );
			}
			temp = 0;
		}
	}
	printf("ok\n");
	return 0;
}