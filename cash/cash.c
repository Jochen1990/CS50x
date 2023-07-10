#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);
    return cents;
}

int calculate_dimes(int cents)
{
    // TODO
    int dimes;
    do
    {
        dimes = cents / 10;
    }
    while (cents < 0);
    return dimes;
}

int calculate_quarters(int cents)
{
    // TODO
    int quarters;
    do
    {
        quarters = cents / 25;
    }
    while (cents < 0);
    return quarters;
}

int calculate_nickels(int cents)
{
    // TODO
    int nickels;
    do
    {
        nickels = cents / 5;
    }
    while (cents < 0);
    return nickels;
}

int calculate_pennies(int cents)
{
    // TODO
    int pennies;
    do
    {
        pennies = cents / 1;
    }
    while (cents < 0);
    return pennies;
}
