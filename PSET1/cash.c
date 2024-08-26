#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n, count = 0;
    do
    {
        n = get_int("Please enter Amount\n");
    }
    while (n <= 0);

    while (n > 0)
    {
        if (n >= 25)
        {
            n = n - 25;
            count++;
            continue;
        }
        if (n >= 10 && n <= 25)
        {
            n = n - 10;
            count++;
            continue;
        }
        if (n >= 5 && n <= 10)
        {
            n = n - 5;
            count++;
            continue;
        }
        if (n >= 1 && n <= 5)
        {
            n = n - 1;
            count++;
            continue;
        }
    }
    printf("%i\n", count);
}