# Реализуй классы Auto и Human. Автомобиль должен иметь
# атрибуты: название, максимальное количество пассажиров. Человек
# должно иметь имя и возраст. Реализуйте возможность добавления
# людей к авто (если оно еще не переполнено), возможность
# посмотреть количество пассажиров (len) и вывод всех пассажиров
# авто(каждый пассажир авто должен поздороваться). Человек
# должна иметь метод hi(поздравления), выводящий ее атрибуты в
# любом формате.

class Auto:
    MAX_PASSENGERS = 5

    def __init__(self, name: str, passengers: "Human | list[Human]"):
        self.name = name
        self.passengers = []
        self.add_passenger(passengers)

    def __str__(self):
        return (f"Название: {self.name}\t\tСейчас в машине: {len(self.passengers)}"
                f"\t\tКоличество мест: {self.MAX_PASSENGERS}")

    def __len__(self):
        return len(self.passengers)

    def add_passenger(self, passenger: "Human | list[Human]"):
        temp_passenger = passenger if isinstance(passenger, list) else [passenger]

        passenger_inside = sum(
            passe in self.passengers
            for passe in temp_passenger
        )

        if (len(temp_passenger) + len(self.passengers) - passenger_inside) > self.MAX_PASSENGERS:
            print(
                f"В машине не хватает места!\n"
                f"В машине сейчас: {len(self)} из {self.MAX_PASSENGERS} мест")
            return

        for passe in temp_passenger:
            if passe in self.passengers:
                print(f"{passe} уже в машине")
                continue
            self.passengers.append(passe)

    def hi_all(self):
        for passe in self.passengers:
            print(passe.hi())


class Human:
    def __init__(self, name: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть меньше 0")
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def hi(self):
        return f"Меня зовут {self.name}\t\tМне {self.age} лет"

h1 = Human("Олег", 20)
print(h1)
print(h1.hi())
h2 = Human("Паша", 25)
h3 = Human("Аня", 19)

print("=" * 20)
auto = Auto("Mazda", [h1, h2, h3])
print(auto)
auto.hi_all()

print("=" * 20)
h4 = Human("Даша", 23)
auto.add_passenger([h1, h4])
print(auto)
auto.hi_all()

print("=" * 20)
h5 = Human("Артём", 25)
h6 = Human("Вова", 26)
auto.add_passenger([h5, h6])

print("=" * 20)
auto.add_passenger(h6)
auto.hi_all()