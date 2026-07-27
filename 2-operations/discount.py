price = input("Введите цену товара: ")
discount = input("Введите скидку: ")

product_with_discount_price = int(price) - int(price) * int(discount) / 100

print("Цена товара с учетом скидки: " + str(product_with_discount_price))    