/* https://www.codeeval.com/open_challenges/3/ */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const int N = 1000;
static const int MAX_NUM_DIGITS = 10;

void mark_primes(char **numbers);
int is_palindrome(int i);

int main(int argc, char **argv)
{
    char *numbers;
    numbers = malloc(N + 1);
    memset(numbers, '1', N);

    mark_primes(&numbers);    

    int i = (N - 1);
    int found;
    for (; (i >= 0) && !found; (found = (numbers[i] == '1') && is_palindrome(i)), i--)
        ;

    printf("%d\n", ++i);

    free(numbers);
    return 0;
}

void mark_primes(char **numbers)
{   
    double first_limit = sqrt(N);
    for (int i = 2; i < first_limit; i++)
    {
        if ((*numbers)[i] == '1')
        {
            for (int j = i*i; j < N; (*numbers)[j] = '0', j+=i)
                ;
        }
    }
}

int is_palindrome(int i)
{
    char *number;
    number = malloc(MAX_NUM_DIGITS + 1);
    memset(number, 0, MAX_NUM_DIGITS);

    sprintf(number, "%d", i);
    int digits = strlen(number);
    int palindrome = 1;
    for (int j = 0; (j < (digits / 2)) && (palindrome == 1); (palindrome = (number[j] == number[digits - j - 1])), j++)
        ;

    free(number);
    return palindrome;
}
