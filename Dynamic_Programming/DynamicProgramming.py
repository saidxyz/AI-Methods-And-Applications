coins = [1, 5, 10, 20]
amount = 1040528

def minimum_number_of_coins(amount, coins):
    # Create a list to remember the minimum coins for each amount
    table  = [float('inf')] * (amount + 1)  # We start by setting everything to a very big number (infinity)
    table [0] = 0  # We need 0 coins to make amount 0

    #Solve for every amount from 1 to the amount we want
    for i in range(1, amount + 1):
        # Try every coin to see if it helps us make this amount with fewer coins
        for coin in coins:
            if i - coin >= 0:  # Only do this if the coin is not too big for the amount
                table [i] = min(table [i], table [i - coin] + 1)  # Use the coin if it gives a better result
    # If we never found a way to make the amount, return -1
    return table [amount] if table [amount] != float('inf') else -1

# Test the function!
print(f"Coins: {coins}, Amount: {amount}")
print(f"The final result: {minimum_number_of_coins(amount, coins)}")