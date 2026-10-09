import math


def area(r):
    '''
    Возвращает площадь круга заданного радиуса
    
        Параметры:
            r: радиус круга
        
        Возвращаемое значение:
            circle_area (float): площадь круга заданного радиуса

        Пример:
            >>> area(2)
            12.566370614359172
    '''
    
    circle_area = math.pi * r * r
    return circle_area


def perimeter(r):
    '''
    Возвращает периметр круга заданного радиуса
    
        Параметры:
            r: радиус круга
        
        Возвращаемое значение:
            perimeter (float): периметр круга заданного радиуса

        Пример:
            >>> perimeter(3)
            18.84955592153876
    '''
    perimeter = 2 * math.pi * r
    return perimeter

