# задание 21.9.1  Создайте метод, который возвращает атрибуты прямоугольника как строку

class Figure:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'

figure = Figure(5, 10, 50, 100)

print(figure)

# задание 21.9.2   На выходе в консоли вам необходимо получить площадь данной фигуры.

class Figures:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height

r1 = Figures(50, 100)
print("Площадь: ", r1.get_area())

# задание 21.9.3   Сделайте вывод о клиентах в консоль.

class Client:
    def __init__(self, name, lastname, town, balance):
        self.name = name
        self.lastname = lastname
        self.town = town
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.lastname}. {self.town}. Баланс: {self.balance} руб."'

client1 = Client('Иван', 'Петров', 'Москва', 50)
print(client1)

# задание 21.9.4   Создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, name, lastname, city):
        self.name = name
        self.lastname = lastname
        self.city = city

    def get_client(self):
        return f'{self.name} {self.lastname}, г. {self.city}'

client1 = Client('Иван', 'Петров', 'Москва')
client2 = Client('Владимир', 'Зайцев', 'Кострома')
client3 = Client('Олеся', 'Янина', 'Новосибирск')

list_clients = [client1, client2, client3]

for i in list_clients:
    print(i.get_client())