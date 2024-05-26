class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fle(self):
        print(f"{self.name} летает!")

    def eat(self):
        print(f"{self.name} ест!")

    def sing(self):
        print(f"{self.voice} поет!")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Цвет: {self.color}")
        print(f"Голос: {self.voice}")

class Pigeon(Bird):
    def __init__(self, name, voice, color,favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f"{self.name} гуляет!")

bird1 = Pigeon("Рыжик", "Кря-кря", "Желтый", "Семечки")

bird2 = Bird("Кеша", "Кря-кря", "Красный")

bird1.sing()
bird1.info()
bird1.walk()


