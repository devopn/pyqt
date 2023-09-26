def calculate_order_cost(menu, orders):
    total_cost = 0
    for i, order in enumerate(orders):
        if order:  # Если заказ не пустой
            flavor, quantity = order.split('\t')
            cost = int(menu[flavor]) * int(quantity)
            total_cost += cost
            print(f"({i + 1}) {flavor}: {cost}")
    return total_cost


def main():
    menu = {}
    orders = []
    while True:
        line = input()
        if line == '.':  # Конец ввода
            break
        elif line == '------------------------':  # Разделитель между меню и заказами
            continue
        elif '\t' in line:  # Если это строка меню
            flavor, price = line.split('\t')
            menu[flavor] = price
        else:  # Заказы
            orders.append(line)

    total_cost = calculate_order_cost(menu, orders)
    print("Итого:", total_cost)


if __name__ == '__main__':
    main()