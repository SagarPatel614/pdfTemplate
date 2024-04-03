def count_coin_combinations(coins, target, index=0):
    # Base case: If the target is 0, there is one valid combination
    if target == 0:
        return 1

    # Initialize the count of combinations
    combinations_count = 0

    # Iterate through the coins starting from the current index
    for i in range(index, len(coins)):
        coin = coins[i]

        # If the current coin does not exceed the remaining target
        if coin <= target:
            # Recursively call the function with the updated target and index
            combinations_count += count_coin_combinations(coins, target - coin, i)

    return combinations_count


# Example usage:
coins = [1, 25, 5]
target_price = 75
result = count_coin_combinations(coins, target_price)
print("Number of combinations:", result)
