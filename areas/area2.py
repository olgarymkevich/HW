from area import Rectangle, Square, Circle

# создаем два прямоугольника

r1 = Rectangle(3, 4)
r2 = Rectangle(12, 5)

# выводим площадь прямоугольников

print(r1.get_area(),
      r2.get_area())

# создаем два квадрата

sq1 = Square(5)
sq2 = Square(10)

# выводим площадь квадратов

print(sq1.get_area_square(),
      sq2.get_area_square())

# создаем два круга

cir1 = Circle(5, 3.14)
cir2 = Circle(6, 3.14)

# выводим площадь круга

print(cir1.get_area_circle(),
      cir2.get_area_circle())

figures = [r1, r2, sq1, sq2, cir1, cir2]
for figure in figures:
      if isinstance(figure, Square):
            print(figure.get_area_square())
      elif isinstance(figure, Rectangle):
            print(figure.get_area())
      else:
            print(figure.get_area_circle())


