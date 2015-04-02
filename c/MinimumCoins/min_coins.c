/* https://www.codeeval.com/open_challenges/74/ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const int LINE_SIZE = 1024;

int main(int argc, char **argv)
{
    FILE *f;

    if (argc < 2 || !(f = fopen(argv[1], "r")))
    {
        fprintf(stderr, "Unable to open file argument\n");
        return 1;
    }

    char *line, *p;
    line = malloc(LINE_SIZE);
    memset(line, 0, strlen(line));
    
    while (fgets(line, LINE_SIZE, f))
    {
        if ((p = strchr(line, '\n')))
            *p = '\0';

        if (line[0] == '\0')
            continue;

        int total = atoi(line);
        int fives = total / 5;
        total = (fives > 0) ? (total % 5) : total;
        int threes = total / 3;
        total = (threes > 0) ? (total % 3) : total;
        printf("%d\n", (fives + threes + total));

    }
    free(line);
    
    return 0;
}
