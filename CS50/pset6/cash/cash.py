from cs50 import get_float

# get amount from user
change = get_float("Change owed: ")
while change < 0:
    change = get_float("Change owed: ")

# coins
coins = [25, 10, 5, 1]
change *= 100

# calculate
numCoins = 0
for coin in coins:
    numCurrCoin = int(change) // coin
    change -= numCurrCoin * coin
    numCoins += numCurrCoin

print(numCoins)