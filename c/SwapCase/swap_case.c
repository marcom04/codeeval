/* https://www.codeeval.com/browse/96/ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const int LINE_SIZE = 1024;
static const int CAPITAL_A = 65;
static const int CAPITAL_Z = 90;
static const int LOWER_A   = 97;
static const int LOWER_Z   = 122;
static const int CASE_DIFF = 32;

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

        char *tmp = line;
        for(; *tmp; tmp++)
        {
            if ((*tmp >= CAPITAL_A) && (*tmp <= CAPITAL_Z))
                (*tmp)+=CASE_DIFF;
            else if ((*tmp >= LOWER_A) && (*tmp <= LOWER_Z))
                (*tmp)-=CASE_DIFF;
        }
        tmp = NULL;
        printf("%s\n", line);

        memset(line, 0, strlen(line));
    }
    
    free(line);
	return 0;
}
