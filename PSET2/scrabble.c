#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int scoreCal(string s);
void winner(int i, int j);

int main(void)
{
    string player1 = get_string("Player 1: ");
    printf("\n");
    string player2 = get_string("Player 2: ");
    printf("\n");
    int score1 = scoreCal(player1);
    int score2 = scoreCal(player2);
    winner(score1, score2);
}

int scoreCal(string s)
{
    int score = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        s[i] = toupper(s[i]);
    }
    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'L' || s[i] == 'N' ||
            s[i] == 'O' || s[i] == 'R' || s[i] == 'S' || s[i] == 'T' || s[i] == 'U')
        {
            score++;
        }
        if (s[i] == 'D' || s[i] == 'G')
        {
            score += 2;
        }
        if (s[i] == 'B' || s[i] == 'C' || s[i] == 'M' || s[i] == 'P')
        {
            score += 3;
        }
        if (s[i] == 'F' || s[i] == 'H' || s[i] == 'V' || s[i] == 'W' || s[i] == 'Y')
        {
            score += 4;
        }
        if (s[i] == 'K')
        {
            score += 5;
        }
        if (s[i] == 'J' || s[i] == 'X')
        {
            score += 8;
        }
        if (s[i] == 'Q' || s[i] == 'Z')
        {
            score += 10;
        }
    }
    return score;
}
void winner(int i, int j)
{
    if (i > j)
    {
        printf("Player 1 wins!");
    }
    if (i < j)
    {
        printf("Player 2 wins!");
    }
    if (i == j)
    {
        printf("Tie!");
    }
    printf("\n");
}