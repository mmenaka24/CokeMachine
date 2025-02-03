def main():
    amountDue = 50
    validCoins = [25, 10, 5]

    while amountDue > 0:
        print("Amount Due: " + str(amountDue))

        coin = int(input("Insert Coin: "))

        if coin in validCoins:
            amountDue -= coin

    change = -amountDue
    print(f"Change Owed: {change}")


main()
