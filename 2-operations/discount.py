price = input("Введите цену товара: ")
discount = input("Введите скидку: ")

discount_price = int(price) * int(discount) / 100

print("Цена товара с учетом скидки: " + str(discount_price))    