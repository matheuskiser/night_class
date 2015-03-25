__author__ = 'matheuskonzeniser'

test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-01", "APPL", 110.61],
    ["2014-06-01", "APPL", 120.22],
    ["2014-06-01", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-01", "MSFT", 21.25],
    ["2014-06-01", "MSFT", 32.53],
    ["2014-06-01", "MSFT", 40.71],
    ["2014-04-01", "BLAH", 19.99],
    ["2014-09-01", "BLAH", 29.99],
]

appl = []

msft = []

for data in test_data:

    temp = []

    if data[1] == "APPL":
        temp.append(data[0])
        temp.append(data[2])
        appl.append(temp)
    elif data[1] == "MSFT":
        temp.append(data[0])
        temp.append(data[2])
        msft.append(temp)

# Version 2

stock_dict = {}
key_holder = []

for stock in test_data:

    if not stock[1] in key_holder:
        temp = []
        temp.append(stock[0])
        temp.append(stock[2])

        stock_dict[stock[1]] = []
        stock_dict[stock[1]].append(temp)
        key_holder.append(stock[1])
    else:
        temp = []
        temp.append(stock[0])
        temp.append(stock[2])
        stock_dict[stock[1]].append(temp)

for key, val in stock_dict.items():
    print key, "=>", val