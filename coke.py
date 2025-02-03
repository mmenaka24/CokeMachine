def main():
    amountDue = 50

    while amountDue > 0:
        print("Amount Due: " + str(amountDue))

        coin = int(input("Insert Coin: "))

        validCoins = [25, 10, 5]

        if coin in validCoins:
            amountDue -= coin

    change = -amountDue
    print("Change Owed: " + str(change))


main()
