food_price = input("Введите траты на еду: ")
transport_price = input("Введите траты на транспорт: ")
entertainment_price = input("Введите траты на развлечения: ")

total_price = int(food_price) + int(transport_price) + int(entertainment_price)

print("Общая сумма трат: " + str(total_price))
print("Средняя сумма трат: " + str(total_price / 3))