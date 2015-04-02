/* https://www.codeeval.com/open_challenges/1/ */

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

        int fizz = atoi(strtok(line, " "));
        int buzz = atoi(strtok(NULL, " "));
        int n = atoi(strtok(NULL, " "));

        for (int i = 1; i <= n; i++)
        {
            if (((i % fizz) != 0) && ((i % buzz) != 0))
                printf("%d", i);
            else
            {
                if ((i % fizz) == 0)
                    printf("%c", 'F');
                if ((i % buzz) == 0)
                    printf("%c", 'B');
            }
            
            printf("%c", ((i < n) ? ' ' : '\n'));
        }
    }
    free(line);
    
    return 0;
}
