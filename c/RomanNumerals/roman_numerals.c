/* https://www.codeeval.com/browse/106/ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const int LINE_SIZE = 1024;

void convert_number(int number);
char* convert_partial(char* roman, int q, int i);
char* append_atoms(char* buf, int arab_atom, int repetitions);
char* detect_roman_atom(int arab_atom);

int main(int argc, char **argv)
{
    FILE *f;
    char line[LINE_SIZE];

    if (argc < 2 || !(f = fopen(argv[1], "r")))
    {
        fprintf(stderr, "Unable to open file argument\n");
        return 1;
    }

    while (fgets(line, LINE_SIZE, f))
    {
        if (line[0] == '\0')
        {
            continue;
        }

        int number = atoi(line);
        if (number == 0)
        {
            printf("**INVALID**\n");
            continue;
        }

        convert_number(number);
    }

    return 0;
}

void convert_number(int number)
{
    char *roman_number = malloc(LINE_SIZE * sizeof(char));
    if (roman_number == NULL)
    {
        printf("malloc error\n");
        return;
    }
    memset(roman_number, 0, strlen(roman_number));

    int divisor = 1000;
    while (divisor > 0)
    {
        int quotient = number / divisor;
        if (quotient > 0)
        {
            roman_number = convert_partial(roman_number, quotient, divisor);
        }
        number = number % divisor;
        divisor /= 10;
    }
    printf("%s\n", roman_number);

    free(roman_number);
}

char* convert_partial(char* buf, int q, int i)
{
    char *tmp = buf;
    if (q < 4)
        tmp = append_atoms(tmp, i, q);
    else if (q == 4)
    {
        tmp = append_atoms(tmp, i, 1);
        tmp = append_atoms(tmp, 5*i, 1);
    }
    else if (q == 9)
    {
        tmp = append_atoms(tmp, i, 1);
        tmp = append_atoms(tmp, 10*i, 1);
    }
    else
    {
        tmp = append_atoms(tmp, 5*i, 1);
        tmp = append_atoms(tmp, i, (q % 5));
    }
    return tmp;
}

char* append_atoms(char* buf, int arab_atom, int repetitions)
{
    char *tmp = buf;
    char *roman_atom = detect_roman_atom(arab_atom);
    for (int i = 0; i < repetitions; i++)
    {
        strcat(tmp, roman_atom);
    }
    return tmp;
}

char* detect_roman_atom(int arab_atom)
{
    switch(arab_atom)
    {
        case 1000:
            return "M";
        case 500:
            return "D";
        case 100:
            return "C";
        case 50:
            return "L";
        case 10:
            return "X";
        case 5:
            return "V";
        case 1:
            return "I";
        default:
            return "";
    }
}
