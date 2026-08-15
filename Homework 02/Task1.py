# Реализуйте класс Shop (магазин), в который можно добавлять
# товары (класс Product). Товар носит название и цену в качестве атрибутов.
# Магазин должен иметь методы для друга всех имеющихся товаров,
# проверки наличия товара (через магический метод __contains__),
# добавление товара.

class Product:
    def __init__(self, name: str, price: float | int):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Название: {self.name}\t\tЦена: {self.price}"


class Shop:
    def __init__(self, products: Product | list[Product]):
        self.products = products.copy() if isinstance(products, list) else [products]

    def __str__(self):
        return ", ".join(prod.name for prod in self.products)

    def __len__(self):
        return len(self.products)

    def __iadd__(self, other):
        items_to_add = other if isinstance(other, list) else [other]
        for item in items_to_add:
            if item not in self.products:
                self.products.append(item)

        return self

    def __contains__(self, item):
        return item in self.products

    def get_all_prod(self):
        print("\n".join(str(prod) for prod in self.products))

    def add_product(self, product: Product | list[Product]):
        self.products += product if isinstance(product, list) else [product]

    def remove_product(self, product: Product | list[Product]):
        temp_prod = product if isinstance(product, list) else [product]
        for prod in temp_prod:
            if prod in self.products:
                self.products.remove(prod)


pd1 = Product("Мясо", 100)
pd2 = Product("Яйца", 200)

shop = Shop([pd1, pd2])

print(pd1 in shop)

shop.get_all_prod()
