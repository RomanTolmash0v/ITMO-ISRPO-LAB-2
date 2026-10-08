# **Документация**
---
## *1. Общее описание решения*
---
Библиотека Python-фунций для вычисления характеристик геометрических фигур (круг, квадрат).
Проект включает 2 модуля:
- 'square.py' -- функции для квадрата
- 'circle.py' -- функции для круга
- 'triangle.py' -- функции для треугольника
- 'rectangle.py' -- функции для прямоугольника

Формулы, используемые в библиотеке:

| Функция  | Круг (circle.py) | Квадрат (square.py) | Треугольник (triangle.py) | Прямоугольник (rectangle.py) | 
| -------- | ---------------- | ------------------- | ------------------------- | ---------------------------- |
| Периметр | 2πR              | 4a                  | a + b + c                 | 2 * (a + b)                  |
| Площадь  | πR²              | a²                  | a * h / 2                 | a * b                        |

## *2. Описание функций*
---

### square.py

#### area()

Возвращает площадь квадрата с заданной стороной

*Пример вызова:*
'''
python3
>>> from square import area
>>> area(10)
100
'''

#### perimeter()

Возвращает периметр квадрата с заданной стороной

*Пример вызова:*
'''
python3
>>> from square import perimeter
>>> perimeter(5)
20
'''

### circle.py

#### area()

Возвращает площадь круга заданного радиуса

*Пример вызова:*
'''
python3
>>> from circle import area
>>> area(4)
50.26548245743669
'''

#### perimeter()

Возвращает периметр круга заданного радиуса

*Пример вызова:*
'''
python3
>>> from circle import perimeter
>>> perimeter(7)
43.982297150257104
'''

### triangle.py

#### area()

Возвращает площадь треугольника по стороне и высоте, опущенной на эту сторону

*Пример вызова:*
'''
python3
>>> from triangle import area
>>> area(1, 2)
1.0
'''

#### perimeter()

Возвращает периметр треугольника с заданными сторонами

*Пример вызова:*
'''
python3
>>> from triangle import perimeter
>>> perimeter(1, 1, 1)
3
'''

### rectangle.py

#### area()

Возвращает площадь прямоугольника со сторонами a и b

*Пример вызова:*
'''
python3
>>> from rectangle import area
>>> area(3, 4)
12
'''

#### perimeter()

Возвращает периметр прямоугольника по длинам двух смежных сторон a и b

*Пример вызова:*
'''
python3
>>> from rectangle import perimeter
>>> perimeter(3, 4)
14
'''


> [!IMPORTANT]
> Аргумент функций должен быть числом неотрицательным.

## История изменения проекта

1d17a5f (HEAD -> master) add README file
5687988 add documentation
5fc132a add function comment in square.py
6569ebd add function comment in circle.py
