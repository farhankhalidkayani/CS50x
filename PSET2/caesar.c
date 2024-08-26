#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digit(string k)
{
    for (int i = 0; i < strlen(k); i++)
    {
        if (!isdigit(k[i]))
        {
            return false;
        }
    }
    return true;
}

void rotate(string text, int k)
{

    for (int i = 0; i < strlen(text); i++)
    {

        if (isalpha(text[i]))
        {
            char result = isupper(text[i]) ? 'A' : 'a';
            text[i] = ((text[i] - result + k) % 26) + result;
        }
    }
    printf("ciphertext: ");
    for (int i = 0; i < strlen(text); i++)
    {
        printf("%c", text[i]);
    }
    printf("\n");
}

int main(int argc, string key[])
{

    if (argc != 2 || !only_digit(key[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string text = get_string("plaintext: ");

    int k = atoi(key[1]);
    rotate(text, k);
}