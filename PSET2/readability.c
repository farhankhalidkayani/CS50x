#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int calculation(int l, int s, int w);
void result(int i);
int main(void)
{

    string t = get_string("Text: ");

    int l = 0, w = 1, s = 0;

    for (int i = 0; i < strlen(t); i++)
    {

        if (isalpha(t[i]) != 0)
        {
            l++;
        }

        if (t[i] == ' ')
        {
            w++;
        }

        if (t[i] == '.' || t[i] == '!' || t[i] == '?')
        {
            s++;
        }
    }
    int index = calculation(l, s, w);

    result(index);
}

int calculation(int l, int s, int w)
{
    float L = ((float) l / (float) w) * 100;
    float S = ((float) s / (float) w) * 100;
    float si = 0.0588 * L - 0.296 * S - 15.8;
    return round(si);
}

void result(int i)
{
    if (i > 16)
    {
        printf("Grade 16+\n");
    }
    else if (i < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", i);
    }
}