from pathlib import Path


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = Path(self.__file_name)
        if not file.exists():
            return []

        with open(self.__file_name, "r") as f:
            shop_store = f.readlines()
        
        # Удаляем пробелы и символы новой строки
        return [line.strip() for line in shop_store]

    def add(self, *products):
        shop_store = self.get_products()
        existing_names = {line.split(", ")[0] for line in shop_store}  # Сохраняем названия существующих продуктов

        for product in products:
            if not isinstance(product, Product):
                continue
            if product.name in existing_names:
                print(f"Продукт '{product.name}' уже есть в магазине")
                continue
            shop_store.append(str(product))

        with open(self.__file_name, "w") as f:
            f.write("\n".join(shop_store) + "\n")  # Записываем обратно в файл


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product("Potato", 50.5, "Vegetables")
    p2 = Product("Spaghetti", 3.4, "Groceries")
    p3 = Product("Potato", 5.5, "Vegetables")  # Попытка добавить тот же продукт с другим весом

    print(p2)  # __str__
    s1.add(p1, p2, p3)  # Добавляем продукты
    print(s1.get_products())  # Выводим все продукты
