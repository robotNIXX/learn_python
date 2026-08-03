CATEGORY_SOUP = "суп"
CATEGORY_DRINK = "напиток"
CATEGORY_DESSERT = "десерт"


def get_drinks():
    return ["чай", "кофе", "сок"]


def get_soups():
    return ["борщ", "щи", "суп-пюре"]


def get_desserts():
    return ["мороженое", "торт", "фрукты"]


def show_menu():
    category = input(
        "Что вы желаете? Можно выбрать категорию: напиток, суп, десерт: "
    ).strip().lower()
    match category:
        case "напиток":
            product = input(
                "Выберите напиток: " + ", ".join(get_drinks()) + ": "
            ).strip()
            return drinks_price(product)
        case "суп":
            product = input(
                "Выберите суп: " + ", ".join(get_soups()) + ": "
            ).strip()
            return soups_price(product)
        case "десерт":
            product = input(
                "Выберите десерт: " + ", ".join(get_desserts()) + ": "
            ).strip()
            return desserts_price(product)
        case _:
            return show_menu()


def drinks_price(product: str):
    match product.lower():
        case "чай":
            return 100
        case "кофе":
            return 150
        case "сок":
            return 200
        case _:
            product = input(
                "Выберите напиток: " + ", ".join(get_drinks()) + ": "
            ).strip()
            return drinks_price(product)


def soups_price(product: str):
    match product.lower():
        case "борщ":
            return 100
        case "щи":
            return 150
        case "суп-пюре":
            return 200
        case _:
            product = input(
                "Выберите суп: " + ", ".join(get_soups()) + ": "
            ).strip()
            return soups_price(product)


def desserts_price(product: str):
    match product.lower():
        case "мороженое":
            return 100
        case "торт":
            return 150
        case "фрукты":
            return 200
        case _:
            product = input(
                "Выберите десерт: " + ", ".join(get_desserts()) + ": "
            ).strip()
            return desserts_price(product)


def main():
    price = show_menu()
    print(f"Цена: {price} рублей")


if __name__ == "__main__":
    main()
