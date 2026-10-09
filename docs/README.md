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

Получает: сторону квадрата a (int / float)

Возвращает: площадь квадрата (int / float)

Возвращает площадь квадрата с заданной стороной

*Пример вызова:*
'''
python3
>>> from square import area
>>> area(10)
100
'''

#### perimeter()

Получает: сторону квадрата a (int / float)

Возвращает: периметр квадрата (int / float)

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

Получает: радиус круга R (int / float)

Возвращает: площадь круга (float)

Возвращает площадь круга заданного радиуса

*Пример вызова:*
'''
python3
>>> from circle import area
>>> area(4)
50.26548245743669
'''

#### perimeter()

Получает: радиус круга R (int / float)

Возвращает: периметр круга (float)

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

Получает: сторону a (int / float) и высоту h (int / float), опущенную на эту сторону

Возвращает: площадь треугольника (float)

Возвращает площадь треугольника по стороне и высоте, опущенной на эту сторону

*Пример вызова:*
'''
python3
>>> from triangle import area
>>> area(1, 2)
1.0
'''

#### perimeter()

Получает: стороны треугольника a, b и c (int / float)

Возвращает: периметр треугольника (int / float)

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

Получает: стороны прямоугольника a и b (int / float)

Возвращает: площадь прямоугольника (int / float)

Возвращает площадь прямоугольника со сторонами a и b

*Пример вызова:*
'''
python3
>>> from rectangle import area
>>> area(3, 4)
12
'''

#### perimeter()

Получает: стороны прямоугольника a и b (int / float)

Возвращает: периметр прямоугольника (int / float)

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

## Как запустить
Для запуска нужен Python 3.

Скачать его можно с официального сайта: https://www.python.org/downloads/

После установки проверьте, что Python работает:
'''
bash
python3 --version
'''

## История изменения проекта

a120804 (HEAD -> main) Add 2 files with docstring from first labwork. Make documentation with pdoc.

5dde16a Lab is done.

1d17a5f add README file

5687988 add documentation

5fc132a add function comment in square.py

6569ebd add function comment in circle.py