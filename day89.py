from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()

for _ in range(N):
    row = input().rsplit(maxsplit=1)
    item_name, net_price = row[0], int(row[1])
    net_price += ordered_dictionary.get(item_name, 0)
    ordered_dictionary[item_name] = net_price
    
    
for item_name, net_price in ordered_dictionary.items():
    print(item_name, net_price)
