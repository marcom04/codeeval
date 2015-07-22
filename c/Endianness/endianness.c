// https://www.codeeval.com/open_challenges/15/

#include <stdio.h>

int main(void) {
    int i = 1;
    char *p = (char *)&i;

    if (p[0] == 1)
        printf("LittleEndian\n");
    else
        printf("BigEndian\n");
}
