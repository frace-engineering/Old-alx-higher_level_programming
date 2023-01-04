#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void hello_write(void)
{
	char s[] = "and that piece of art is useful - Dora Korpar, 2015-10-19";
	int len = strlen(s);
	write(2, s, len);
	printf("\n");
}
