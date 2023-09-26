def solve():
    with open("prices.txt", 'r') as file:
        prices = file.readlines()
        if not prices:
            print(0)
            return
        sum = 0.0
        for i in prices:
            name, amount, price = i.split("\t")
            sum+= int(amount)*float(price) 

        print("{:.2f}".format(round(sum,2)))


solve()