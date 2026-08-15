class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f"Название: {self.name}\n"
                f"Автор: {self.author}\n"
                f"Страниц: {self.pages}")

    def __len__(self):
        return self.pages

    def print_book(self):
        print(self.name)
        print(self.author)
        print(self.pages)


book1 = Book("One Piece", "Oda", 1000)

print("-" * 20)
book1.print_book()
print("-" * 20)
print(book1)
print("-" * 20)
print(len(book1))
print("-" * 20)

print("\n\n\n")


# # =============================================================================================

class Student1:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Оценки: {(", ".join(str(grade) for grade in self.grades))
                if self.grades else "Нет оценок"}")

    def __len__(self):
        return len(self.grades)

    def add_grade(self, grade: int | list[int]):
        if isinstance(grade, int):
            self.grades.append(grade)
        else:
            self.grades += grade

    def average(self):
        return f"Средняя оценка: {0 if not self else sum(self.grades) / len(self)}"


don = Student1("Don", [])
anton = Student1("Anton", [10])
jon = Student1("Jon", [12, 10, 8])

print("-" * 20)
print(don)
print("-" * 20)
print(anton)
print("-" * 20)
print(jon)
print("-" * 20)
anton.add_grade(5)
print(anton)
print("-" * 20)
anton.add_grade([8, 10])
print(anton)
print(f"Количество оценок: {len(anton)}")
print(anton.average())
print("-" * 20)
print(don)
print(don.average())

print("\n\n\n")


# =============================================================================================


class Student2:
    def __init__(self, name: str, group: "Group | None" = None):
        self.name = name
        self.group = None
        if group is not None:
            group.add_student(self)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Группа: {self.group.name if self.group is not None else "Отсутствует"}")

    def add_group(self, group: "Group"):
        group.add_student(self)

    def remove_group(self):
        if self.group is not None:
            self.group.remove_student(self)


class Group:
    def __init__(self, name: str, students: Student2 | list[Student2] | None = None):
        self.name = name
        self.students: list[Student2] = []

        if students is not None:
            self.add_student(students)

    def __str__(self):
        return (f"Группа: {self.name}\n"
                f"В группе: {", ".join(str(st.name) for st in self.students)}")

    def __len__(self):
        return len(self.students)

    def add_student(self, student: Student2 | list[Student2]):
        temp_st = student if isinstance(student, list) else [student]
        for st in temp_st:
            if st in self.students:
                continue
            if st.group is not None:
                st.group.remove_student(st)

            self.students.append(st)
            st.group = self

    def remove_student(self, student: Student2 | list[Student2]):
        temp_st = student if isinstance(student, list) else [student]
        for st in temp_st:
            if st in self.students:
                self.students.remove(st)
                st.group = None

    def find_student(self, student: Student2):
        if student in self.students:
            print(student)
        else:
            print("Студента нет в этой группе")


st1 = Student2("Алексей")
st2 = Student2("Гоша")

g1 = Group("Группа 1")
print("=" * 20, "> В1\n", g1)
g2 = Group("Группа 2", st2)
print("=" * 20, "> В2\n", g2)
g3 = Group("Группа 3", [st1, st2])
print("=" * 20, "> В3\n", g3)

g2.add_student(st1)
print("=" * 20, "> В4\n", g2)
g3.add_student(st1)
st3 = Student2("Паша", g3)
print("=" * 20, "> В5\n", g3)
print("=" * 20, "> В6\n", st3)
print(f"В группе сейчас {len(g3)} человек")
print("=" * 20)
g2.find_student(st3)
print("=" * 20)
g3.find_student(st3)

print("\n\n\n")


# =============================================================================================


class Product:
    def __init__(self, name: str, price: float | int):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Название: {self.name}\n Цена: {self.price}"


class Cart:
    def __init__(self, products: Product | list[Product]):
        self.products = products.copy() if isinstance(products, list) else [products]

    def __str__(self):
        return f"{", ".join(prod.name for prod in self.products)}"

    def __len__(self):
        return len(self.products)

    def __iadd__(self, other):
        items_to_add = other if isinstance(other, list) else [other]
        for item in items_to_add:
            if item not in self.products:
                self.products.append(item)

        return self

    def add_product(self, product: Product | list[Product]):
        self.products += product if isinstance(product, list) else [product]

    def remove_product(self, product: Product | list[Product]):
        temp_prod = product.copy() if isinstance(product, list) else [product]
        for prod in temp_prod:
            if prod in self.products:
                self.products.remove(prod)

    def total_price(self):
        return sum(prod.price for prod in self.products)


prod1 = Product("Молоко", 100)
prod2 = Product("Мясо", 250.9)
prod3 = Product("Яйца", 80.3)
prod4 = Product("Вода", 33.3)

cart = Cart([prod1, prod2])
print(cart)
cart.add_product(prod3)
print(cart)
cart.remove_product([prod2, prod3])
print(cart)
cart += [prod2, prod3]
print(cart)
cart += prod4
print(cart)
print("Общая стоимость:", cart.total_price())
