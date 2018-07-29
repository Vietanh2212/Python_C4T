prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stocks = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for items ,price, stock in zip(prices.keys(), prices.values(), stocks.values()):
    print("{0} {1}".format("•", items), "{0} {1} : {2}".format("•", "price", price),
          "{0} {1} : {2}".format("•", "stock", stock), sep="\n")
    print()

total = 0
for num in prices:
    a = prices[num] * stocks[num]
    print("The value of all", num + "s", "is: ", a)
    total += a

print(total)