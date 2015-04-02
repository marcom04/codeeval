/* https://www.codeeval.com/browse/40/ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const int LINE_SIZE = 1024;

char count_occurrences(char *string, char character);

int main(int argc, char **argv)
{
	FILE *f;
    char line[LINE_SIZE], *p;

    if (argc < 2 || !(f = fopen(argv[1], "r")))
    {
        fprintf(stderr, "Unable to open file argument\n");
        return 1;
    }

    while (fgets(line, LINE_SIZE, f))
    {
    	if ((p = strchr(line, '\n')))
    		*p = '\0';

        if (line[0] == '\0')
            continue;

        char position = (char)((int)'0');
        int i = 0;
        for(; (count_occurrences(line, position) == line[i]) && (i < strlen(line)); i++, position = (char)(((int)'0')+i));

        printf("%d\n", (i == strlen(line)));
    }

	return 0;
}

char count_occurrences(char *string, char character)
{
	int count = 0;
	for(; *string; count += *string == character, string++);
	return (char) (((int)'0')+count);
}
