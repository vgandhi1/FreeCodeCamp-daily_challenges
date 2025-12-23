"""
Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	1.00 USD
EUR	1.10 USD
GBP	1.25 USD
JPY	0.0070 USD
CAD	0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.
"""
def buy_items(funds, items):

    currency_to_usd = {
    "USD": 1.00,
    "EUR": 1.10,
    "GBP": 1.25,
    "JPY": 0.0070,
    "CAD": 0.75
    }
    n = len(items)


    budget = float(funds[0])*currency_to_usd[funds[1]]

    #below list-comprehension creates the item amount in USD
    #items_amt = [float(x[0])*currency_to_usd[x[1]] for x in items]

    item_sum = 0
    no_items = 0
    

    #while True:
    #for i, item in enumerate(items_amt):
    for i, (amount, currency) in enumerate(items):
        price_usd = float(amount) * currency_to_usd[currency]

        if item_sum + price_usd <= budget:
            item_sum += price_usd
            no_items = i + 1
        else:
            break   
        
    if no_items == n:
        return "Buy them all!"
    else:
        return f"Buy the first {no_items} items."

print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]))
print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]))
print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))
print(buy_items(["10.00", "USD"], [["50.00", "USD"]])
)

"""
Tests
Passed:1. buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) should return "Buy the first 2 items.".
Passed:2. buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) should return "Buy them all!".
Passed:3. buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]) should return "Buy the first 3 items.".
Passed:4. buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]) should return "Buy them all!".
Passed:5. buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]) should return "Buy the first 5 items.".
"""
